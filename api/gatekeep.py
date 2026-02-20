from http.server import BaseHTTPRequestHandler
import urllib.parse
import math
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        typer_username = params.get('typer', [''])[0]

        gatekeep_skill = random.random() * 10000
        placement = gatekeep_skill / 10000 * 100

        if gatekeep_skill >= 9900:
          response = f"yeah yeah keep gatekeeping, you might aswell gatekeep everything, youre on some kinda leaderboard for gatekeeping for sure, youre better than {placement}% of gatekeepers"
        elif gatekeep_skill >= 6500:
          response = f"of course you'd be gatekeeping, youre better than {placement}% of gatekeepers"
        elif gatekeep_skill >= 3000:
          response = f"keep it up, one day you might be able to gatekeep more, youre better than {placement}% of gatekeepers"
        elif gatekeep_skill >= 1000:
          response = f"why... how could you do this.. I thought you were a good person who didnt gatekeep, youre better than {placement}% of gatekeepers"
        elif gatekeep_skill >= 100:
          response = f"you cant gatekeep anything, youre in the bottom {placement}% of gatekeepers"
        elif gatekeep_skill <  100:
          response = f"HAHA, YOU REALLY THOUGHT YOU COULD GATEKEEP ANYTHING, YOU ROLLED BELOW 100 OUT OF 10000, IM CRYING, youre in the bottom {placement}% of gatekeepers"
        

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())
