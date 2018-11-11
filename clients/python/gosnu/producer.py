class Producer():
    def __init__(self, tcp_client):
        self.tcp_client = tcp_client

    def consume(self):
        self.tcp_client.sendall("bees".encode())

        # Read data from the TCP server and close the connection
        return self.tcp_client.recv(1024)
