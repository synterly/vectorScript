from http.server import BaseHTTPRequestHandler
import urllib.parse
import math
import random

def gaslighting_ability(name):
    if name.lower() == "synterly":
        return 90
    else:
        return random.random() * 100

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        typer_username = params.get('typer', [''])[0]
        target_username = params.get('target', [''])[0]

        typer_power = gaslighting_ability(typer_username)
        if target_username.lower() == typer_username.lower():
            response = f"{typer_username} tried to gaslight... themselves? I'm not sure..."
        else:
            target_power = gaslighting_ability(target_username)
            certainty = ( typer_power / target_power ) * 100
            if target_power > typer_power:
                response = f"{typer_username} failed to gaslight {target_username}, they are {certainty:.1f}% convinced"
            elif target_power < typer_power:
                response = f"{typer_username}, gaslit {target_username}, they are {certainty:.1f}% convinced"
            elif target_power == typer_power:
                response = f"{typer_username} and {target_username} tied, with {typer_power:.1f}% gaslighting ability, they are equally dumb dumb and tricked eachother."
                
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())
