import socket
import os
import threading

def handle_request(client_socket, request):
    # ambil nama file dari request yang dikirim oleh client
    filename = request.split()[1][1:]

    # Cek apakah file ada di server
    if os.path.isfile(filename):
        # membaca isi file, jika file ada
        with open(filename, 'rb') as file:
            response_data = file.read()

        # kirim response dengan status code 200 OK dan isi file
        response = b"HTTP/1.1 200 OK " + response_data
    else:
        # kirim response dengan status code 404 Not Found jika file tidak ada
        response = b"HTTP/1.1 404 not found \nMessage: File not found"

    # kirim response ke client
    client_socket.sendall(response)

    # tutup koneksi socket
    client_socket.close()

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    try:
        # ambil request dari client dan menampilkannya ke terminal
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        # panggil fungsi handle_request untuk menangani request dari client
        handle_request(client_socket, request)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # tutup koneksi socket setelah selesai menangani request
        client_socket.close()

def main():
    host = '127.0.0.1'  # Localhost
    port = 6789

    # membuat socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # meng-assign host dan port ke server socket
    server_socket.bind((host, port))

    # server dijalankan untuk menerima koneksi dari client
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        # menerima koneksi dari client dan menampung socket dan address client
        client_socket, client_address = server_socket.accept()

        # membuat thread baru untuk menangani request dari client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        
        # menjalankan thread
        client_thread.start()

if __name__ == "__main__":
    main()
