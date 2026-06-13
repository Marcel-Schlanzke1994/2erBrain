local M = {}

function M.run(code, env)
  local safe = {
    assert = assert,
    ipairs = ipairs,
    pairs = pairs,
    tostring = tostring,
    tonumber = tonumber,
    math = math,
    string = string,
    table = table,
  }
  for key, value in pairs(env or {}) do
    safe[key] = value
  end
  local chunk, err = load(code, "sandbox", "t", safe)
  if not chunk then
    return false, err
  end
  return pcall(chunk)
end

return M
