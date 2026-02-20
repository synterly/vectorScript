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

        typer_power = girlboss_power(typer_username)
        if target_username.lower() == typer_username.lower():
            response = f"{typer_username} is totally girlbossing out right now, wowza! {typer_power:.0f} girlboss potential!"
        else:
            target_power = girlboss_power(target_username)
            if target_power > typer_power:
                response = f"uh oh! {typer_username}, you got outgirlbossed by {target_username}"
            elif target_power < typer_power:
                response = f"{typer_username}, totally out girlbossed {target_username}"
            elif target_power == typer_power:
                response = f"{typer_username} and {target_username} tied, with {typer_power:.0f}% potential to girlboss, they should girlboss together and not against eachother, there is a 2^-53 chance of this code executing, this occurence is less likely than exactly perfectly guessing the order of all the cards in a deck of cards."
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())
