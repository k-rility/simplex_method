#include <boost/program_options.hpp>
#include <iostream>

#include "server_interface.hpp"

namespace po = boost::program_options;

int main(int argc, char* argv[]) {
  //  log_init();
  po::options_description desc("Allowed options");
  desc.add_options()("help,h", "All commands");
  po::variables_map vm;
  po::store(po::parse_command_line(argc, argv, desc), vm);
  po::notify(vm);
  if (vm.count("help")) {
    std::cout << desc << std::endl;
    return 0;
  }

  run_server("127.0.0.1", 8080);
}