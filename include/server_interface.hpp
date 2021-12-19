
// asio && http

#include <boost/asio/ip/tcp.hpp>
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/version.hpp>
#include <boost/thread.hpp>

// std

#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <utility>
#include <memory>

using tcp = boost::asio::ip::tcp;
namespace net = boost::asio;
namespace http = boost::beast::http;
namespace beast = boost::beast;

inline const std::string ip_address = "127.0.0.1";
inline const unsigned long port = 8080;

class http_server {
 public:
  http_server()
      : acceptor__(context__,
                   tcp::endpoint(net::ip::make_address(ip_address), port)) {}

  ~http_server() = default;

  //  http_server(const http_server& other) = delete;
  //
  //  http_server operator=(const http_server& other) = delete;
  //
  //  http_server(http_server&& other) = delete;
  //
  //  http_server operator=(http_server&& other) = delete;

  void run_server();

 private:
  net::io_context context__{1};
  tcp::acceptor acceptor__;
};