#ifndef SUGGESTION_HPP
#define SUGGESTION_HPP

#include <nlohmann/json.hpp>

using json = nlohmann::json;

class suggestion {
 public:
  suggestion() = default;

  json make_suggestion(const json&)const;

 private:
  json suggestion__;
};

#endif  // SUGGESTION_HPP
