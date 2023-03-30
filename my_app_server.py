from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer as TCPServer
from socketserver import TCPServer as UDPServer
import sys

PORT = 8000
HOST = "localhost"

REDIRECT_URL="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"

def run_tcp_server():
    class tcp_redirect_handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            # Redirect HTTP status
            self.send_response(301)  
            self.send_header('Location', REDIRECT_URL)
            self.end_headers()

    with TCPServer((HOST, PORT), tcp_redirect_handler) as httpd:
        print("My HTTP Server - TCP serving at port", PORT)
        httpd.serve_forever()


def run_rudp_server():
    class rudp_redirect_handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            # Redirect HTTP status
            self.send_response(301)  
            self.send_header('Location', REDIRECT_URL)
            self.end_headers()


    with UDPServer((HOST, PORT), rudp_redirect_handler) as httpd:
        print("My HTTP Server - RUDP serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    if "RUDP" == sys.argv[1]:
        print("Serving HTTP using RUDP")
        run_rudp_server()
    elif "TCP" == sys.argv[1]:
        print("Serving HTTP using TCP")
        run_tcp_server()
    else:
        print("Usage: python3 my_app_server.py <RUDP|TCP>")
