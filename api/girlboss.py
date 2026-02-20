from http.server import BaseHTTPRequestHandler
import urllib.parse
import math
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        response = " wow youre girlbossing so hard!"
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())
