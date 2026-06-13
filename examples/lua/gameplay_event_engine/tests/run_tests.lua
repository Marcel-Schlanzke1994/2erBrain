package.path = './src/?.lua;./tests/?.lua;' .. package.path
local files={'test_event_engine','test_rewards','test_cooldowns','test_sandbox'}
for _,f in ipairs(files) do require(f) end
print('lua tests passed')
