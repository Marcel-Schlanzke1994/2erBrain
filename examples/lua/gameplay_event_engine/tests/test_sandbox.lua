local s=require('sandbox'); local ok=s.run('x=1'); assert(ok); local ok2=s.run('return os.execute("echo bad")'); assert(ok2==false)
