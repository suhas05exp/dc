import socket

def start_client():
    host = '127.0.0.1'  # Server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello from client!")
        data = s.recv(1024)

    print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    start_client()
