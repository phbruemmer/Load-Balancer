import socket
import asyncio
import threading


class ServerConfig:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        # std. configuration
        self.max_clients = 32

    class TaskManager:
        def __init__(self):
            self.threads = 0
            self.thread_pool = []

        def start_client_thread(self, target, *args) -> None:
            client_thread = threading.Thread(target=self.client_thread_wrapper, args=(target, args))
            client_thread.start()

        def client_thread_wrapper(self, arg_data) -> None:
            target, args = arg_data
            print(f"[client_thread_wrapper] new thread started to execute function at {target}")
            target(args)
            print("[client_thread_wrapper] closing thread...")
            self.update_thread_pool()
            self.threads -= 1

        def update_thread_pool(self) -> None:
            print("[update_thread_pool] updating thread pool...")
            self.thread_pool = [thread for thread in self.thread_pool if thread.is_alive()]
            print("[update_thread_pool] thread pool up to date.")

    class ServerNodes:
        def __init__(self):
            self.nodes = []

    def handle_client(self):
        pass

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.ip, self.port))
            sock.listen(self.max_clients)

            while True:
                client_sock, client_addr = sock.accept()
                self.TaskManager.start_client_thread(self.handle_client, (client_sock, client_addr))


if __name__ == '__main__':
    server_config = ServerConfig(ip="127.0.0.1", port=8000)
    server_config.run()
