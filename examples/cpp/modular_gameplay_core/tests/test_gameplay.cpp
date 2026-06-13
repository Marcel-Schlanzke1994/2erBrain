#include "gameplay/event_bus.hpp"
#include "gameplay/health_component.hpp"
#include "gameplay/lua_runtime_adapter.hpp"
#include <cassert>
int main(){ gameplay::HealthComponent hp(10); hp.damage(4); assert(hp.current()==6); hp.heal(99); assert(hp.current()==10); hp.damage(20); assert(!hp.alive()); gameplay::EventBus bus; int seen=0; bus.subscribe("hit",[&](const gameplay::Event&e){seen=e.value;}); assert(bus.publish({"hit",3})==1 && seen==3); gameplay::LuaRuntimeAdapter lua; assert(!lua.run("return 1").ok); }
