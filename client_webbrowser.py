import socket
import sys
import webbrowser
import os
import time

def main():
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        return

    # Extract command line arguments
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))

        # Send the HTTP GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
        client_socket.sendall(request.encode('utf-8'))

        # Receive the response
        response = client_socket.recv(4096)
        
        # Check if the response is an HTML page
        if response.startswith(b"HTTP/1.1 200 OK"):
            print("HTTP/1.1 200 OK")
            print("Opening the HTML content in a web browser...")
            # Write the HTML content to a temporary file
            with open("temp.html", "wb") as temp_file:
                temp_file.write(response)
            
            # Construct the URL
            url = f"file://{os.path.abspath('temp.html')}"

            # Open the URL in the default web browser
            webbrowser.open(url)
        else:
            print(response.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
