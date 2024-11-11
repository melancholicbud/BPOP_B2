import socket
import time

UDP_IP = 'localhost'
UDP_PORT = 8883

def run_client(ip, port):
    time.sleep(2)
    MESSAGE = u"""Echo-service ($) "Hello World!"""
    sock = socket.socket(socket.AF_INET, # ipv4 
                         socket.SOCK_DGRAM) # udp
    server = (ip, port)
    for line in MESSAGE.split(' '):
        data = line.encode('utf-8')
        sock.sendto(data, server)
        print(f'Client || On Server {server} sent: {repr(data)}')
        response, address = sock.recvfrom(1024) # size of buffer: 1024
        print(f"Client || Data received: {repr(response.decode('utf-8'))} from {address}")
    print("End of client")

def run_server(ip, port):
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    server = (ip, port)
    sock.bind(server)
    print(f'Starting an echo-server: {server}')

    while True:
        data, address = sock.recvfrom(1024) # size of buffer 1024
        print(f'Client || On Server {server} sent: {repr(data)}')
        sock.sendto(data, address)
        print(f"Client || Data received: {repr(data)} from {address}")

if __name__ == "__main__":
    from multiprocessing import Process
    client = Process(target=run_client, args=(UDP_IP, UDP_PORT,))
    server = Process(target=run_server, args=(UDP_IP, UDP_PORT,))
    server.start()
    client.start()
    client.join()
    server.terminate()