import socket

from gosnu.consumer import Consumer
from gosnu.producer import Producer


class Connection():
    def __init__(self, ip, port=8081):
        self.ip = ip
        self.port = port
        self.tcp_client = None

    def connect(self):
        # Initialize a TCP client socket using SOCK_STREAM
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establish connection to TCP server and exchange data
        self.tcp_client.connect((self.ip, self.port))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.tcp_client.close()

    def Producer(self):
        return Producer(self.ip)

    def Consumer(self, callback=print):
        return Consumer(self.tcp_client, callback=callback)
