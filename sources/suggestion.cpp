#include "suggestion.hpp"

json make_suggestion(const json& input) const {
  json res;
  res["suggestions"] = json::array();
  json item;
  size_t pos = 0;
  for (const auto& i : suggestion__) {
    if (input["input"] == i.at["id"]) {
      item["text"] = i.at["name"];
      item["position"] = pos;
      res["suggestion"].emplace_back(item);
    }
  }
  return res;
}
