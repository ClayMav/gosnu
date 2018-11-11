class Consumer():
    def __init__(self, tcp_client, callback=print):
        self.tcp_client = tcp_client
        self.callback = callback

    def consume(self):
        self.tcp_client.send("give\n".encode())

        # Read data from the TCP server and close the connection
        answer = self.tcp_client.recv(1024)
        return answer

    def receive(self, contents):
        self.callback(contents)
