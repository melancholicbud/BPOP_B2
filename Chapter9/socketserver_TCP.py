from socketserver import (BaseRequestHandler, TCPServer)
from sockettest2 import run_client

TCP_IP = 'localhost'
TCP_PORT = 8000

class EchoTCP(BaseRequestHandler):
    def handle(self):
        print(f'Server || Connection is established with: {self.client_address}')
        while True:
            msg = self.request.recv(1024)
            if not msg:
                break
            print(f'Server || Message incoming: "{msg}" from {self.client_address}')
            print(f'Server || Echo-message: "{msg}" sent to {self.client_address}')
            self.request.send(msg)

if __name__ == "__main__":
    from multiprocessing import Process
    # tcp-server
    server = TCPServer((TCP_IP, TCP_PORT), EchoTCP)
    client = Process(target=run_client, args=(TCP_IP, TCP_PORT,))
    client.start()
    server.serve_forever()