#pragma once
#include <string>
namespace gameplay { struct ScriptResult{bool ok; std::string message;}; class LuaRuntimeAdapter{ public: ScriptResult run(std::string_view) { return {false,"Lua runtime not linked in this reference build"}; } }; }
