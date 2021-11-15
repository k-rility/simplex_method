#include "server_interface.hpp"

void handle_request(http::request<http::string_body>&& request) {
  //  http::serializer<http::string_body>
  std::cout << request.body() << std::endl;
}

void do_session(tcp::socket& socket) {
  beast::error_code ec_code;
  beast::flat_buffer buffer;

  for (;;) {
    http::request<http::string_body> request;
    http::read(socket, buf  fer, request, ec_code);

    if (ec_code == http::error::end_of_stream) {
      std::cerr << "error end of stream\n" << ec_code.message() << std::endl;
      break;
    }
    handle_request(std::move(request));
    if (ec_code) {
      std::cerr << ec_code.message() << std::endl;
      return;
    }
  }
}

void run_server(const std::string& ip, unsigned long port) {
  tcp::endpoint endpoint(net::ip::make_address(ip), port);

  boost::system::error_code ec;
  boost::asio::io_context io_context{1};

  tcp::acceptor acceptor{io_context, endpoint};

  for (;;) {
    tcp::socket socket(io_context);
    acceptor.accept(socket);
    std::thread(std::bind(std::ref(do_session), std::move(socket))).detach();
  }
}
