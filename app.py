#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Web Server</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 600px; margin: 0 auto; text-align: center; }
                h1 { color: #333; }
                .info { background: #f0f0f0; padding: 20px; border-radius: 5px; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Web Server is Running!</h1>
                <div class="info">
                    <p><strong>Server:</strong> Python HTTP Server</p>
                    <p><strong>Instance:</strong> Amazon Linux EC2</p>
                    <p><strong>Port:</strong> 80</p>
                </div>
                <p>Your Terraform deployment was successful!</p>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), SimpleHandler)
    print("Server running on port 80...")
    server.serve_forever()