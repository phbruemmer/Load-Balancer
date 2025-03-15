import socket
import asyncio
import threading


class NodeData:
    def __init__(self, ip, port, node_id):
        self.ip = ip
        self.port = port
        self.node_id = node_id

        self.max_node_connections = 16

        self.connections = 0
        self.connected_clients = []

        self.task_manager = self.TaskManager

    class TaskManager:
        def __init__(self, node_data):
            self.node_data = node_data

            self.threads = 0
            self.max_threads = 4
            self.thread_pool = []

        def create_new_thread(self, target, *args) -> None:
            if self.threads < self.max_threads:
                new_thread = threading.Thread(target=target, args=args)
                new_thread.start()
                self.threads += 1
            else:
                print("[create_new_thread] reached max thread limit.")

        def thread_wrapper(self, initial_target, *args) -> None:
            initial_target(args)
            self.update_thread_pool()
            self.threads -= 1

        def update_thread_pool(self) -> None:
            self.thread_pool = [thread for thread in self.thread_pool if thread.is_alive()]
            print("[update_thread_pool] updated thread pool.")

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.ip, self.port))
            # sock.listen(self.max_node_connections)


if __name__ == '__main__':
    pass
