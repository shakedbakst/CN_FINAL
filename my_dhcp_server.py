import socket
import random

MAX_BYTES = 1024

SERVER_PORT = 8068

class DHCP_server(object):

    def server(self):
        print("DHCP server is starting...\n")
        
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('localhost', SERVER_PORT))

        while 1:
            try:
                while 1:
                    try:
                        print("Wait DHCP request.")
                        data, dest = s.recvfrom(MAX_BYTES)
                        print("Receive DHCP request.")
                        #print(data)

                        print("Send DHCP pack.\n")
                        data = DHCP_server.pack_get()
                        s.sendto(data, dest)
                        break
                    except:
                        raise
            except:
                raise

    def pack_get():
        subnet_mask = "255.255.255.0"
        router = "192.168.1.1"
        lease = "1"
        ip = f"192.168.1.{random.randrange(255)}"

        package = str.encode("|".join([subnet_mask, router, lease, ip]))

        return package


if __name__ == '__main__':
    dhcp_server = DHCP_server()
    dhcp_server.server()
