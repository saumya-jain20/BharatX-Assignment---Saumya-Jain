import http.server
import socketserver
import ssl
import threading
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [PORT %(port)d] %(message)s')

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Log incoming requests with port info
        logging.info(f"Received GET request from {self.client_address}", extra={'port': self.server.server_port})
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')  # Add content type header
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def run_server(port, cert_path, key_path):
    try:
        httpd = http.server.HTTPServer(("", port), RequestHandler)
        
        # Create SSL context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=cert_path, keyfile=key_path)
        
        # Wrap the socket with SSL context
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        
        logging.info(f"Server started and serving on port {port}.", extra={'port': port})
        httpd.serve_forever()
    except Exception as e:
        logging.error(f"Error starting server on port {port}: {e}", extra={'port': port})

if __name__ == "__main__":
    # List of ports for multiple instances
    ports = [8000, 8001, 8002]
    
    # Paths of certificate and key
    cert_path = "C:\\Users\\Asus\\OneDrive\\Desktop\\BharatX\\cert.pem"  # Update to the correct cert path
    key_path = "C:\\Users\\Asus\\OneDrive\\Desktop\\BharatX\\key.pem"    # Update to the correct key path
    
    threads = []
    
    # Starting each server instance in a separate thread
    for port in ports:
        thread = threading.Thread(target=run_server, args=(port, cert_path, key_path))
        thread.daemon = True  # Ensure threads close with the main program
        thread.start()
        threads.append(thread)
        logging.info(f"Started server on port {port}.", extra={'port': port})

    # Keep the main thread alive to allow the servers to run
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        logging.info("Shutting down servers.")
