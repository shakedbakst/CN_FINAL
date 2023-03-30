import socket

MAX_BYTES = 1024

MY_DHCP_SERVER_HOST="localhost"
MY_DHCP_SERVER_PORT=8068

class DHCP_client(object):
    def client():
        print("DHCP client is starting...\n")
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
        print("Send DHCP request.")
        data = DHCP_client.request_get();
        s.sendto((data), (MY_DHCP_SERVER_HOST, MY_DHCP_SERVER_PORT))
        
        data,address = s.recvfrom(MAX_BYTES)
        print("Receive DHCP pack.\n", address)
        ip = data.decode().split('|')[3]
        return ip

    def request_get():
        subnet_mask = "255.255.255.0"
        router = "192.168.1.1"
        lease = "1"
        server_ip = ""

        package = str.encode("|".join([subnet_mask, router, lease, server_ip]))

        return package

	

