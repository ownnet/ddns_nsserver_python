#!/usr/bin/python
#https://github.com/pebble/cloudpebble-nameserver
from dnslib import *
from dnslib.server import DNSHandler, DNSServer
import re
import conf
from GetRecord import *
from Log import *
import time



class Resolve(object):        
    def resolve(self, request, handler):
        """
        @type request: DNSRecord
        @type handler: DNSHandler
        """
        t = time.time();
        name = request.q.qname
        name = str(name)[:-1]

        qtype = {
            1:'A', 2:'NS', 5:'CNAME', 6:'SOA', 12:'PTR', 15:'MX',
                 16:'TXT', 17:'RP', 18:'AFSDB', 24:'SIG', 25:'KEY', 28:'AAAA',
                 29:'LOC', 33:'SRV', 35:'NAPTR', 36:'KX', 37:'CERT', 38:'A6',
                 39:'DNAME', 41:'OPT', 42:'APL', 43:'DS', 44:'SSHFP',
                 45:'IPSECKEY', 46:'RRSIG', 47:'NSEC', 48:'DNSKEY', 49:'DHCID',
                 50:'NSEC3', 51:'NSEC3PARAM', 52:'TLSA', 55:'HIP', 99:'SPF',
                 249:'TKEY', 250:'TSIG', 251:'IXFR', 252:'AXFR', 255:'ANY',
                 257:'CAA', 32768:'TA', 32769:'DLV'
        }
        
        #print(request.q.qtype)
        reply = request.reply()
        record = GetRecord().get(name,qtype[request.q.qtype],False)
        
        if request.q.qtype == QTYPE.A:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.A, rdata=A(item['value'])))
        if request.q.qtype == QTYPE.NS:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.NS, rdata=NS(item['value'])))
        if request.q.qtype == QTYPE.CNAME:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.CNAME, rdata=CNAME(item['value'])))
        if request.q.qtype == QTYPE.MX:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.MX, rdata=MX(item['value'],preference=10)))
        if request.q.qtype == QTYPE.TXT:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.TXT, rdata=TXT(item['value'])))
        if request.q.qtype == QTYPE.AAAA:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.AAAA, rdata=AAAA(item['value'])))       
        if request.q.qtype == QTYPE.SRV:
            for item in record:
                reply.add_answer(RR(request.q.qname, ttl=int(item['ttl']), rtype=QTYPE.SRV, rdata=SRV(item['value'])))
        
        Log.log('processing time:'+str(time.time() - t))
        return reply
                

class Server():
    def start(self):
        print("Server running at "+str(conf.PORT))
        server = DNSServer(Resolve(), port=conf.PORT)
        server.start()

if __name__ == "__main__":
    Server().start()
    #print(RCache().get('ddns.imgroot.bid'))
    #Log.log("2");
    #RCache().set('name','value','120')
    