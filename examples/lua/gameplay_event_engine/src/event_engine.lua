local M={}
function M.new() return {events={}} end
function M.register(engine,name,handler) assert(type(handler)=='function','handler required'); engine.events[name]=handler end
function M.emit(engine,name,ctx) local h=engine.events[name]; if not h then return false,'missing_event' end; local ok,res=pcall(h,ctx or {}); if not ok then return false,res end; return true,res end
return M
