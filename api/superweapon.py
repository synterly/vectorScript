from http.server import BaseHTTPRequestHandler
import urllib.parse
import math

employees = ["synterly", "smarticles101"]

def superweapon_power(typer_str, target_str):
    chars1 = list(typer_str.lower())
    chars2 = list(target_str.lower())
    all_chars = sorted(set(chars1 + chars2))
    n1, n2 = len(chars1), len(chars2)
    
    vec1 = [chars1.count(c) / n1 if n1 > 0 else 0 for c in all_chars]
    vec2 = [chars2.count(c) / n2 if n2 > 0 else 0 for c in all_chars]
    
    diff_sum_sq = sum((v2 - v1)**2 for v1, v2 in zip(vec1, vec2))
    return math.sqrt(diff_sum_sq)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        typer_username = params.get('typer', [''])[0]
        target_username = params.get('target', [''])[0]

        if target_username.lower() in employees
            response = "ERROR: you cannot fire the bank's weapon at bank employees!"
        else if not typer_username or not target_username:
            response = "it missed (invalid username), try aiming better next time haha."
        else:
            power = superweapon_power(typer_username, target_username)
            response = f"{typer_username} fired the weapon of the bank of Loki at {target_username}, it had {power:.3f} Joules of force."
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
        self.wfile.write(response.encode())

