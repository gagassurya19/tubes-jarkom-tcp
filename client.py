import socket
import sys
import webbrowser
import os

def main():
    if len(sys.argv) != 4:
        print("Penggunaan: client.py <server_host> <server_port> <filename>")
        return

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_host, server_port))

        request = f"GET /{filename} HTTP/1.1\nHost: {server_host}:{server_port}\n"
        client_socket.sendall(request.encode('utf-8'))
        print(f"Request: {request.encode('utf-8')}")

        response = client_socket.recv(1024)
        
        if response.startswith(b"HTTP/1.1 200 OK"):
            print("HTTP/1.1 200 OK")
            print("Message: Membuka file HTML di browser...")

            with open("temp.html", "wb") as temp_file:
                temp_file.write(response)
            
            url = f"file://{os.path.abspath('temp.html')}"

            webbrowser.open(url)
        else:
            print(response.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
