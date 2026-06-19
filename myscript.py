from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
    <script src="/script.js"></script>
</head>
<body style="display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
    <h1 id="hello" style="cursor:pointer;">Hello World</h1>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/script.js":
            script_path = os.path.join(os.path.dirname(__file__), "script.js")
            with open(script_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML.encode())

HTTPServer(("localhost", 8080), Handler).serve_forever()