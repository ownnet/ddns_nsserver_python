import conf
import memcache

class MemcachedCache:
    mc = ''

    def __init__(self, *args, **kwargs):
        self.mc = memcache.Client([conf.MEMCACHED_HOST+':'+str(conf.MEMCACHED_PORT)])

    def get(self,key):
        value = self.mc.get(key)
        if value:
            return True,value
        else:
            return False,None
        
    def set(self,key,value,time=0):
        return self.mc.set(key,value,time)

    def add(self,key,value,time=0):
        return self.mc.add(key,value,time)
    
    def update(self,key,value,time=0):
        return self.mc.replace(key,value,time)
    
    def exists(self,key):
        ok,_ = self.get(key)
        return ok;

    def delete(self,key):
        return self.mc.delete(key)
    
    def incr(self,key,amount = 1):
        return self.mc.incr(key,amount)
        
    def decr(self,key,amount = 1):
        return self.mc.decr(key,amount)
    
    def keyList(self,prefix):
        # slab_list = 
        # a = self.mc.get_stats('cachedump 1 100')
        # 

        a = self.mc.get_stats('sizes')
        print(a[0])
        # for k in a[0][1]:
        #     print (k.decode());
        return False

    def dbSize(self):
        a = self.mc.get_stats()
        return a[0][1][b'bytes'].decode()