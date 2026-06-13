local rewards={rift={xp=100,gold=25}, small={xp=10,gold=1}}
return { resolve=function(name) local r=rewards[name]; if not r then return nil,'unknown_reward' end; return {xp=r.xp,gold=r.gold} end }
