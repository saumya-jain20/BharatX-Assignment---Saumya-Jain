# Multi-Server HTTPS Setup with SSL/TLS Encryption

## Project Overview
This project demonstrates the setup of multiple HTTPS servers running concurrently on different ports using Python. Each server handles GET requests, logs client information, and sends a "Hello, world!" response over secure SSL/TLS connections. The servers are managed using threading to enable concurrency. The project includes detailed logging, error handling, and graceful shutdown capabilities.

## Features
- **Multiple HTTPS Servers**: Servers run securely using SSL/TLS encryption.
- **Concurrency with Threading**: Each server instance runs on a separate thread, enabling concurrent execution.
- **Detailed Logging**: Logs client requests with port-specific information, including timestamps.
- **Graceful Shutdown**: The servers shut down safely when interrupted (e.g., using `Ctrl+C`).
- **Custom Request Handling**: Responds with "Hello, world!" for GET requests.

## Requirements
- Python 3.x
- SSL/TLS certificates (`cert.pem` and `key.pem`)

## Installation
1. Clone the repository or download the project files to your local machine.
2. Ensure you have Python 3.x installed.
3. Place your SSL/TLS certificate files (`cert.pem` and `key.pem`) in the same directory as the code, or update the paths in the script.

## Running the Project
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the servers:
   ```bash
   python assignment.py
   ```

The script will start servers on ports 8000, 8001, and 8002, each running in its own thread.

## Logging
The logs provide detailed information about incoming requests, including the client’s IP address and the port number of the server handling the request. Logs are written to the console and include timestamps.

Example log:
```
2024-12-06 10:15:30,123 - [PORT 8000] Received GET request from ('127.0.0.1', 12345)
```

## Stopping the Servers
To stop the servers, press `Ctrl+C` in the terminal. The servers will shut down gracefully.

## Code Structure
- **https_server.py**: The main script that sets up and runs the HTTPS servers.
- **RequestHandler**: Custom handler for processing GET requests.
- **run_server**: Function to initialize and start a server on a specific port.

## Use Cases
- **Microservices Architecture**: Host multiple services securely on separate ports.
- **API Gateways**: Serve secure API endpoints concurrently.
- **Testing & Debugging**: Simulate multi-server environments for system testing.

---

### Notes
- Update the paths to your SSL/TLS certificate files before running the project.
- The servers will run indefinitely until manually stopped, and they will handle multiple incoming requests concurrently.

---
