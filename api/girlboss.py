from http.server import BaseHTTPRequestHandler
import urllib.parse
import math
import random

def girlboss_power():
    return random.random()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        typer_username = params.get('typer', [''])[0]
        target_username = params.get('target', [''])[0]

        typer_power = girlboss_power()
        if not target_username:
            response = f"{typer_username} is totally girlbossing out right now, wowza! {typer_power} girlboss potential!"
        else:
            target_power = girlboss_power()
            if target_power > typer_power:
                response = f"uh oh! {typer_username}, you got outgirlbossed, with {typer_power} vs {target_power}"
            elif target_power < typer_power:
                response = f"{typer_username} totally out girlbossed {target_username} with {typer_power} vs {target_power}"
            elif target_power == typer_power:
                response = f"{typer_username} and {target_username} tied, with {typer_power}, they should girlboss together and not against eachother"
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())
