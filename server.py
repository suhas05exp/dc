import socket

def start_server():
    host = '127.0.0.1'  # localhost (use '0.0.0.0' to allow external connections)
    port = 65432        # non-privileged port > 1023

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server is listening on {host}:{port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received from client: {data.decode()}")
                conn.sendall(b"Hello from server!")

if __name__ == "__main__":
    start_server()
