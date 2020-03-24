from socket import *
import socket
import threading
import logging
import time
import sys

from file_machine import Machine

m = Machine()

class Process(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(2048)
            if data:
                d = data.decode()
                res = m.proses(d)
                self.connection.sendall(res.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            cli = Process(self.connection, self.client_address)
            cli.start()
            self.the_clients.append(cli)

if __name__ == "__main__":
    print("Waiting a connection")
    s = Server()
    s.start()
