class NoneCache:
    def get(self,key):
        return False,None
        
    def set(self,key,value,time=None):
        return False

    def add(self,key,value,time=None):
        return False
    
    def update(self,key,value,time=None):
        return False
    
    def exists(self,key):
        return False

    def delete(self,key):
        return False
    
    def incr(self,key,amount = 1):
        return False
        
    def decr(self,key,amount = 1):
        return False
    
    def keyList(self,prefix):
        return False

    def dbSize(self):
        return False