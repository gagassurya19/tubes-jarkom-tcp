import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Penggunaan: client.py server_host server_port filename")
        return

    # ambil value dari command dengan menggunakan index dari array sys.argv
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # membuat socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # menggunakan try-except untuk menangani error
    try:
        # koneksi socket ke server sesuai dengan host dan port
        client_socket.connect((server_host, server_port))

        # mengirim request dengan methode GET ke server
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
        client_socket.sendall(request.encode('utf-8'))

        # menampung response dari server
        response = client_socket.recv(4096)
        print(response.decode('utf-8'))
    except Exception as e:
        # menampilkan error jika terjadi error
        print(f"Error: {e}")
    finally:
        # tutup koneksi socket setiap semua kode sudah dijalankan
        client_socket.close()

if __name__ == "__main__":
    main()
