local r=require('reward_engine'); local got=r.resolve('rift'); assert(got.xp==100); local none,err=r.resolve('x'); assert(none==nil and err)
