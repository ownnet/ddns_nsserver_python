import conf
if conf.CACHE_TYPE == 0:
    from cache.NoneCache import *
    cache_class = "NoneCache"
if conf.CACHE_TYPE == 1:
    from cache.NoneCache import *
    cache_class = "MemcachedCache"
if conf.CACHE_TYPE == 2:
    from cache.RedisCache import *
    cache_class = "RedisCache"
    

'''cacheFunc = eval(cache_class+"()")
print (cacheFunc.get('num1'))    
#print(RedisCache().get('num1'))'''

class RCache(eval(cache_class)):
    def __init__(self):
        super(RCache, self).__init__()
        pass;
    
#print(RCache().get('num1'))