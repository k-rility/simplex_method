#include "server_interface.hpp"

#include "suggestion.hpp"

//void suggestions_update(const std::shared_ptr<Suggestion>& suggestion,
//                        const std::shared_ptr<std::timed_mutex>& mutex) {
//  for (;;) {
//    mutex->lock();
//    suggestion.
//    mutex->unlock();
//  }
//}

std::string convert_to_str(const json& j) {
  std::string convert_str = "";
  for (auto const& i : j.at("suggestions")) {
    convert_str += std::to_string(i.at("position").get<unsigned long>()) +
                   "   " + i.at("text").get<std::string>() + "\n\n";
  }
  return convert_str;
}

struct send_lambda {
  tcp::socket& socket__;
  bool& close__;
  beast::error_code& ec__;

  explicit send_lambda(tcp::socket& socket, bool& close, beast::error_code& ec)
      : socket__(socket), close__(close), ec__(ec) {}

  template <bool isRequest, class Body, class Fields>

  void operator()(http::message<isRequest, Body, Fields>&& message) {
    close__ = message.need_eof();
    http::serializer<isRequest, Body, Fields> serializer{message};
    http::write(socket__, serializer, ec__);
    socket__.close();
  }
};

void handle_request(http::request<http::string_body>&& request,
                    send_lambda& send) {
  http::response<http::string_body> answer{http::status::ok, request.version()};

  suggestion suggestion("../misc/collections.json");

  auto const bad_request = [&request](beast::string_view why) {
    http::response<http::string_body> res{http::status::bad_request,
                                          request.version()};
    res.body() = std::string(why);
    res.prepare_payload();
    return res;
  };

  auto const not_found = [&request](beast::string_view route) {
    http::response<http::string_body> res{http::status::not_found,
                                          request.version()};
    res.body() = "Not found: " + std::string(route);
    res.prepare_payload();
    return res;
  };

  if (request.method() != http::verb::post) {
    return send(bad_request("Wrong request method"));
  }

  if (request.target() != "/v1/vpi/suggest") {
    return send(not_found(request.target()));
  }

  json input;
  input["input"] = request.body();
  json ans = suggestion.make_suggestion(input);
  answer.body() = convert_to_str(ans);
  answer.prepare_payload();

  return send(std::move(answer));
}

void do_session(tcp::socket& socket) {
  beast::flat_buffer buffer;
  beast::error_code ec_code;
  bool close = false;

  http::request<http::string_body> request;
  http::read(socket, buffer, request, ec_code);

  if (ec_code) {
    std::cout << ec_code.message() << std::endl;
    return;
  }

  send_lambda lambda(socket, close, ec_code);

  handle_request(std::move(request), lambda);
}

void http_server::run_server() {
  std::shared_ptr<std::timed_mutex> mutex =
      std::make_shared<std::timed_mutex>();
  std::shared_ptr<Suggestion> suggestion = std::make_shared<Suggestion>();
  std::thread{
      suggestions_update,
  };
  for (;;) {
    tcp::socket socket{context__};
    acceptor__.accept(socket);
    std::thread{std::bind(&do_session, std::move(socket))}.detach();
  }
}