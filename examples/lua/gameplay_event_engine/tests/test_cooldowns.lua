local c=require('cooldowns'); local s={}; c.start(s,'a',10,5); assert(c.is_active(s,'a',12)); assert(not c.is_active(s,'a',16))
