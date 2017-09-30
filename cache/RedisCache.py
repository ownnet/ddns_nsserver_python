import conf
import redis

redisClient = redis.StrictRedis(host=conf.REDIS_HOST,port=conf.REDIS_PORT,db=conf.REDIS_DB_NUM,password=conf.REDIS_PASSWORD)

class RedisCache:
    def __init__(self):
        self.r = redisClient
    
    def get(self,key):
        try:
            value = self.r.get(key)
        except redis.exceptions.ResponseError:
            return False,'Function Error'            
        if type(value) == bytes:
            return True,value.decode()
        else:
            return False,value
        
    def set(self,key,value,time=None):
        return self.r.set(key, value, ex=time)

    def add(self,key,value,time=None):
        return self.r.set(key, value, ex=time,nx=True)
    
    def update(self,key,value,time=None):
        return self.r.set(key, value, ex=time,xx=True)
    
    def exists(self,key):
        ok,_ = self.get(key)
        return ok;

    def delete(self,key):
        return self.r.delete(key)
    
    def incr(self,key,amount = 1):
        try:
            if type(amount)  == int:
                return self.r.incrby(key, amount)
            else:
                return self.r.incrbyfloat(key, amount)
        except redis.exceptions.ResponseError:
            return False
            
        
    def decr(self,key,amount = 1):
        if type(amount)  == int:
            return self.r.decr(key, amount)
        else:
            return self.r.incrbyfloat(key, -amount)
    
        
    def keyList(self,prefix):
        rst = self.r.keys(prefix + "*");        
        return list(map(lambda x:x.decode(),rst))
    def dbSize(self):
        return self.r.dbsize()
    