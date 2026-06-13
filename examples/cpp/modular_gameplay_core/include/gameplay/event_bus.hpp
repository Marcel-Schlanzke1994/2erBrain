#pragma once
#include <functional>
#include <string>
#include <unordered_map>
#include <vector>

namespace gameplay {
struct Event {
    std::string name;
    int value{0};
};

class EventBus {
  public:
    using Handler = std::function<void(const Event &)>;
    void subscribe(std::string name, Handler handler);
    int publish(const Event &event) const;

  private:
    std::unordered_map<std::string, std::vector<Handler>> handlers_;
};
} // namespace gameplay
