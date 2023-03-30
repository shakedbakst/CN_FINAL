from dnslib.server import DNSServer, DNSRecord
from dnslib.dns import RR
import time

class MyAppServerResolver:
    MY_APP_SERVER="myappserver.com"
    MY_APP_SERVER_IP="127.0.0.1"

    def resolve(self, request, handler):
            reply = request.reply()
            reply.add_answer(*RR.fromZone(f"{self.MY_APP_SERVER}. 60 A {self.MY_APP_SERVER_IP}"))
            return reply


print("Running MyDnsServer... listening on port 8053")
resolver = MyAppServerResolver()
server = DNSServer(resolver, port=8053, address="localhost", tcp=True)
server.start_thread()
while server.isAlive():
    time.sleep(1)
server.stop() 
