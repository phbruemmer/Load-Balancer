import socket
import asyncio
import threading


class NodeData:
    def __init__(self, ip, port, node_id):
        self.ip = ip
        self.port = port
        self.node_id = node_id

        self.task_manager = self.TaskManager

    class TaskManager:
        def __init__(self, node_data):
            self.node_data = node_data

            self.threads = 0
            self.async_tasks = 0

            self.max_async_tasks = 4
            self.max_threads = 4

            self.thread_pool = []

        def create_new_thread(self, target, *args) -> None:
            if self.threads < self.max_threads:
                new_thread = threading.Thread(target=target, args=args)
                new_thread.start()
                self.threads += 1

        def thread_wrapper(self, initial_target, *args) -> None:
            initial_target(args)
            self.threads -= 1

        def update_thread_pool(self) -> None:
            self.thread_pool = [thread for thread in self.thread_pool if thread.is_alive()]
            print("[update_thread_pool] updated thread pool.")



        def create_new_async(self):
            pass


if __name__ == '__main__':
    pass
