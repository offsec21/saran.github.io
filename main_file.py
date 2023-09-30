import http.server
import socketserver
import os

# Specify the directory where HTML files are located
html_dir = os.path.dirname(os.path.abspath(__file__))

# Set up a basic HTTP server to serve the HTML files
port = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/login":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(html_dir, "login.html"), "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/contact":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(html_dir, "contact.html"), "rb") as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()

with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
