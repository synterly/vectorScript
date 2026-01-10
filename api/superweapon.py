from http.server import BaseHTTPRequestHandler
import urllib.parse
import math

def superweapon_power(typer_str, target_str):
    chars1 = list(typer_str.lower())
    chars2 = list(target_str.lower())
    
    all_chars = sorted(set(chars1 + chars2))
    n1, n2 = len(chars1), len(chars2)
    
    vec1 = [chars1.count(c) / n1 if n1 > 0 else 0 for c in all_chars]
    vec2 = [chars2.count(c) / n2 if n2 > 0 else 0 for c in all_chars]
    
    # Manual norm: sqrt(sum((v2-v1)^2))
    diff_sum_sq = sum((v2 - v1)**2 for v1, v2 in zip(vec1, vec2))
    return math.sqrt(diff_sum_sq)

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
            response = f"{typer_username} -> {target_username}: {power:.3f}"
            
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

