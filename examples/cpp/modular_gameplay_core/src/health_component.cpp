#include "gameplay/health_component.hpp"
#include <algorithm>
namespace gameplay { HealthComponent::HealthComponent(int max):max_(std::max(1,max)),current_(max_){} void HealthComponent::damage(int amount){ if(amount>0) current_=std::max(0,current_-amount); } void HealthComponent::heal(int amount){ if(amount>0) current_=std::min(max_,current_+amount); } int HealthComponent::current() const{return current_;} bool HealthComponent::alive() const{return current_>0;} }
