import socket


SERVER_IP = "127.0.0.1"
SERVER_PORT = 8000


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_IP, SERVER_PORT))
        sock.send(b"Test msg")


if __name__ == '__main__':
    run_client()
