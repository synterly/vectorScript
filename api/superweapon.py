from http.server import BaseHTTPRequestHandler
import urllib.parse
import math
import random

def superweapon_power(typer_str, target_str):
    def weighted_chars(s):
        chars = list(s.lower())
        weights = [ 1.0 - random.random() * i/len(chars) for i in range(len(chars))]
        return {c: sum(w for char, w in zip(chars, weights) if char == c) for c in set(chars)}
    
    freq1 = weighted_chars(typer_str)
    freq2 = weighted_chars(target_str)
 
    all_chars = set(freq1) | set(freq2)

    total_w1 = sum(freq1.values())
    total_w2 = sum(freq2.values())
    
    vec1 = [freq1.get(c, 0) / total_w1 if total_w1 > 0 else 0 for c in all_chars]
    vec2 = [freq2.get(c, 0) / total_w2 if total_w2 > 0 else 0 for c in all_chars]
    
    diff_sum_sq = sum((v2 - v1)**2 for v1, v2 in zip(vec1, vec2))
    return math.sqrt(diff_sum_sq)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        employees = ["synterly", "aubsec", "scavengeremain", "smarticles101", "bank", "torypixels"]
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        typer_username = params.get('typer', [''])[0]
        target_username = params.get('target', [''])[0]

        if target_username.lower() in employees:
            response = "ERROR: you cannot fire the bank's weapon at bank employees!"
        elif typer_username.lower() in employees:
            power = superweapon_power(typer_username, target_username) * 10
            response = f"{typer_username} fired the weapon of the bank of Loki at {target_username}, it had {power:.3f} Newtons of force."    
        elif typer_username == target_username:
            response = "ERROR: dont target yourself dummy"
        elif not typer_username or not target_username:
            response = "it missed (invalid username), try aiming better next time haha."
        else:
            power = superweapon_power(typer_username, target_username)
            response = f"{typer_username} fired the weapon of the bank of Loki at {target_username}, it had {power:.3f} Newtons of force."
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())
