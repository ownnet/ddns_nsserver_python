from db import *
from cache.RCache import *
from Log import *
import json

class Record(BashModel):
    id = IntegerField(unique=True)
    user_id = IntegerField()
    host = CharField()
    type = CharField()
    value = CharField()
    ttl = CharField()
    auth_code = CharField()
    options = CharField()
    status = IntegerField()
    
    def getRecordFromHostName(self, name, qtype):
        rst = []
        for item in Record.select().where((Record.host == name)& (Record.type == qtype) & (Record.status == 1)):
            rst.append(item)
        return rst
        
class GetRecord():
    def __init__(self):
        pass;
    def get(self,name,qtype,recursion = False):
        return self.getFromCache(name, qtype, recursion)
    
    def getFromCache(self,name,qtype,recursion):
        key = name + '->' + qtype
        Log.log ("Cache key:" + key)
        status,value = RCache().get(key)
        if status:
            return eval(value)
        else:
            Log.log('Cache Miss')
            v = self.getFromDB(name, qtype , recursion)
            RCache().set(name,v,3600)
            return v

    def getFromDB(self,name,qtype,recursion = False):
        Log.log("Try:"+ name)
        rst = Record().getRecordFromHostName(name, qtype)
        record_list = []
        if len(rst) != 0:
            for item in rst:
                tmp = dict()
                tmp['value'] = item.value
                tmp['ttl'] = item.ttl
                record_list.append(tmp)
            return record_list
        else:
            if recursion:
                next_name = name.split(sep=".", maxsplit=1)
                if len(next_name) == 1:
                    Log.log("Done,NotFound")
                    return []
                else:
                    Log.log("NotFound")
                    return self.get(next_name[1], qtype, recursion = True)
            else:
                if name.find('*') == -1:
                    next_name = name.split(sep=".", maxsplit=1)
                    if len(next_name) == 1:
                        Log.log("Done,NotTry")
                        return []
                    else:
                        name = '*.' + next_name[1]
                else:
                    next_name = name.split(sep=".", maxsplit=2)
                    if len(next_name) <= 2:
                        Log.log("Done,NotTry")
                        return []
                    else:
                        name = '*.' + next_name[-1]
                    
                return self.getFromDB(name, qtype)