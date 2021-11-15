#ifndef SERVER_INTERFACE_HPP_
#define SERVER_INTERFACE_HPP_

#include <boost/asio/ip/tcp.hpp>
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/version.hpp>
#include <iostream>
#include <string>
#include <thread>
#include <utility>

using tcp = boost::asio::ip::tcp;
namespace http = boost::beast::http;
namespace net = boost::asio;
namespace beast = boost::beast;



void Write(const http::request<http::string_body>& );


void handle_request(http::request<http::string_body>&&);

void run_server(const std::string&, unsigned long);

void do_session(tcp::socket&);

#endif  // SERVER_INTERFACE_HPP_
