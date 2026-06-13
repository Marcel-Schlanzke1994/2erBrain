local M={}
function M.is_active(store,key,now) local until_time=store[key]; return until_time ~= nil and until_time > now end
function M.start(store,key,now,seconds) store[key]=now+seconds; return store[key] end
return M
