import socket
import sys
import webbrowser
import os

def main():
    if len(sys.argv) != 4:
        print("Penggunaan: client.py <server_host> <server_port> <filename>")
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
        request = f"GET /{filename} HTTP/1.1\nHost: {server_host}:{server_port}\n"
        client_socket.sendall(request.encode('utf-8'))
        print(f"Request: {request.encode('utf-8')}")

        # menampung response dari server
        response = client_socket.recv(4096)
        
        # cek apakah response yang diterima adalah HTTP/1.1 200 OK
        if response.startswith(b"HTTP/1.1 200 OK"):
            print("HTTP/1.1 200 OK")
            print("Message: Membuka file HTML di browser...")

            # membuat file baru dengan nama temp.html dan menuliskan response ke file tersebut
            with open("temp.html", "wb") as temp_file:
                temp_file.write(response)
            
            # assign path file ke variable url
            url = f"file://{os.path.abspath('temp.html')}"

            # membuka file temp.html di web browser
            webbrowser.open(url)
        else:
            # menampilkan response jika response yang diterima bukan HTTP/1.1 200 OK
            print(response.decode('utf-8'))
    except Exception as e:
        # menampilkan error jika terjadi error
        print(f"Error: {e}")
    finally:
        # tutup koneksi socket setiap semua kode sudah dijalankan
        client_socket.close()

if __name__ == "__main__":
    main()
