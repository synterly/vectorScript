from http.server import BaseHTTPRequestHandler
import urllib.parse
import numpy as np
from collections import Counter

def superweapon_power(user_str, target_str):
    # Character-level vectorization (alnum chars only)
    chars1 = [c.lower() for c in user_str if c.isalnum()]
    chars2 = [c.lower() for c in target_str if c.isalnum()]
    
    # Count frequencies → normalize to probability vectors
    all_chars = set(chars1 + chars2)
    vec1 = np.array([chars1.count(c) / len(chars1) if len(chars1) > 0 else 0 for c in all_chars])
    vec2 = np.array([chars2.count(c) / len(chars2) if len(chars2) > 0 else 0 for c in all_chars])
    
    # Directional resultant magnitude (target - typer)
    resultant = vec2 - vec1
    return np.linalg.norm(resultant)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        typer_username = params.get('typer', [''])[0]
        target_username = params.get('target', [''])[0]
        
        if not typer_username or not target_username:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write("it missed (invalid username)".encode())
            return
        
        try:
            power = superweapon_power(typer_username, target_username)
            response = f"{power:.3f}"
            
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(response.encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write("it missed (invalid username)".encode())

