import requests
import urllib.request
import sys
import time

from my_dns_client import my_dns_query
from my_dhcp_client import DHCP_client

MY_APP_SERVER_HOST, MY_APP_SERVER_PORT = ("localhost", 8000)
DOWNLOAD_FILE_NAME="video.mp4"
INTERVAL_SLEEP_MILSEC=0.1

def RUDP_download_from_http(url):
    # 64Kb Chunks
    CHUNKS=65536

    # UDP based HTTP GET request.
    get_response = requests.get(url,stream=True)

    print(f"Downloading file {DOWNLOAD_FILE_NAME}")

    with open(DOWNLOAD_FILE_NAME, 'wb') as f:
        # Implementing FLOW-CONTROL, by division to chunks
        for chunk in get_response.iter_content(chunk_size=CHUNKS):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                # Flowcontrol - add sleep to allow chunk queue to fill up
                time.sleep(INTERVAL_SLEEP_MILSEC)


def TCP_download_from_http(url):
    print(f"Downloading file {DOWNLOAD_FILE_NAME}")
  
    # TCP based file download over HTTP - TCP reliability guaranteed!
    urllib.request.urlretrieve(url, DOWNLOAD_FILE_NAME)


if __name__ == '__main__':
    # Get IP address by DHCP:
    print("Get IP address from MyDhcpServer server")
    ip = DHCP_client.client()
    # Set own ip address
    print(f"My ip is {ip}")

    # Using MyDnsServer to resolve address of myappserver.com 
    print("DNS Resolving myappserver.com")
    my_app_server_ip = my_dns_query("localhost", 8053, "myappserver.com")
    print(f"myappserver.com is {my_app_server_ip}")
    HTTP_SERVER_URL = f"http://{my_app_server_ip}:{MY_APP_SERVER_PORT}"


    if "RUDP" == sys.argv[1]:
        print("Download video from MyAppServer using RUDP")
        RUDP_download_from_http(HTTP_SERVER_URL)
    elif "TCP" == sys.argv[1]:
        print("Download video from MyAppServer using TCP")
        TCP_download_from_http(HTTP_SERVER_URL)
    else:
        print("Usage: python3 my_app_client.py <RUDP|TCP>")
   
