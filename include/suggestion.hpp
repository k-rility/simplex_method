#ifndef SUGGESTION_HPP
#define SUGGESTION_HPP

#include <boost/filesystem.hpp>
#include <exception>
#include <fstream>
#include <iomanip>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
namespace fs = boost::filesystem;

class Suggestion {
 public:
  Suggestion() = default;
  explicit Suggestion(const fs::path& json_file_path) {
    std::ifstream fin{json_file_path};

    if (!fin.is_open()) {
      throw std::runtime_error{"error path: " + json_file_path.string()};
    }

    fin >> suggestions__;
    fin.close();
  }

  json make_suggestion(const json& input) const {
    json result;
    result["suggestions"] = json::array();
    json item;
    size_t pos = 0;
    for (const auto& i : suggestions__.at("suggestions")) {
      if (input["input"] == i.at("id")) {
        item["text"] = i.at("name");
        item["position"] = pos;
        ++pos;
        result["suggestions"].emplace_back(item);
      }
    }
    return result;
  }

  json get_suggestion() const { return suggestions__; }

 private:
  json suggestions__;
};

#endif  // SUGGESTION_HPP
