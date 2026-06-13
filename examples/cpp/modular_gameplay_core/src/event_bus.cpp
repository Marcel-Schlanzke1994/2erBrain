#include "gameplay/event_bus.hpp"
namespace gameplay { void EventBus::subscribe(std::string name, Handler h){ handlers_[std::move(name)].push_back(std::move(h)); } int EventBus::publish(const Event& e) const{ auto it=handlers_.find(e.name); if(it==handlers_.end()) return 0; for(auto const& h: it->second) h(e); return static_cast<int>(it->second.size()); } }
