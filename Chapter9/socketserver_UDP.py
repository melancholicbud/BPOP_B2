from socketserver import (BaseRequestHandler, UDPServer)
from sockettest import run_client

UDP_IP = 'localhost'
UDP_PORT = 8000

class EchoUDP(BaseRequestHandler):
    def handle(self): 
        print(f'Server || Connection is established: {self.client_address}') 
        msg, sock = self.request 
        print(f'Server || Message is received: {msg.decode("utf-8")} from {self.client_address}') 
        print(f'Server || Echo-message: "{msg.decode("utf-8")}" sent to {self.client_address}') 
        sock.sendto(msg, self.client_address)

if __name__ == "__main__" :
    from multiprocessing import Process
    server = UDPServer((UDP_IP, UDP_PORT), EchoUDP) 
    client = Process(target=run_client, args=(UDP_IP, UDP_PORT))
    client.start()
    server.serve_forever()