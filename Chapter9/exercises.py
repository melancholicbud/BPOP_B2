"""ex. 1: TCP-chat"""
# server
import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Message from client: {message}")
                broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()
print("The server is running and waiting for connection...")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    print(f"Client is established: {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()


# client
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Server connection error.")
            sock.close()
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
print("Connected to chat.")

thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

while True:
    message = input("Input a message: ")
    client_socket.send(message.encode('utf-8'))


"""ex. 2: UDP-chat"""
# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))
print("UDP server is established.")

while True:
    message, addr = server.recvfrom(1024)
    print(f"Message from: {addr}: {message.decode('utf-8')}")
    server.sendto("Message is received".encode('utf-8'), addr)

# client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Input a message: ")
    client.sendto(message.encode('utf-8'), ('localhost', 12345))
    response, _ = client.recvfrom(1024)
    print(f"Server response: {response.decode('utf-8')}")

"""ex. 3: UDP file transfer"""
# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))
print("The UDP server is running to transfer the file.")

with open("received_file.txt", "wb") as file:
    while True:
        data, addr = server.recvfrom(1024)
        if not data:
            break
        file.write(data)

# client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open("file_to_send.txt", "rb") as file:
    for data in file:
        client.sendto(data, ('localhost', 12345))

"""ex. 4: TCP file transfer"""
# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("The TCP server is running to transfer the file..")

conn, addr = server.accept()
with open("received_file.txt", "wb") as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)
conn.close()

# client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

with open("file_to_send.txt", "rb") as file:
    for data in file:
        client.send(data)
client.close()


"""ex. 5: tic-tac-toe online"""
import socket
import select

def create_connection():
    host = '127.0.0.1'  # Replace with the server's IP address
    port = 12345  # Replace with the desired port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    return client_socket

def send_message(socket, message):
    socket.sendall(message.encode())

def receive_message(socket):
    data = socket.recv(1024).decode()
    return data

def play_game(socket):
    board = [' '] * 9
    player_symbol = 'X'  # Assume player is X, server is O

    while True:
        # Receive the current board state from the server
        board_str = receive_message(socket)
        board = list(board_str)

        # Display the board
        print_board(board)

        # Check if the game is over
        if check_win(board, 'O'):
            print("You lose!")
            break
        elif check_win(board, 'X'):
            print("You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Make a move
        move = input("Enter your move (1-9): ")
        send_message(socket, move)

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

if __name__ == "__main__":
    client_socket = create_connection()
    play_game(client_socket)
    client_socket.close()

"""ex. 6: sea fight online"""
import socket
import random

def create_connection():
    host = '127.0.0.1'  # Replace with the server's IP address
    port = 12345  # Replace with the desired port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    return client_socket

def send_message(socket, message):
    socket.sendall(message.encode())

def receive_message(socket):
    data = socket.recv(1024).decode()
    return data

def create_board():
    board = [['O'] * 10 for _ in range(10)]
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def place_ships(board):
    ship_sizes = [5, 4, 3, 3, 2]
    for size in ship_sizes:
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9 - size + 1)
            orientation = random.choice(['horizontal', 'vertical'])

            if orientation == 'horizontal':
                if all(board[row][col + i] == 'O' for i in range(size)):
                    for i in range(size):
                        board[row][col + i] = 'S'
                    break
            else:
                if all(board[row + i][col] == 'O' for i in range(size)):
                    for i in range(size):
                        board[row + i][col] = 'S'
                    break

def play_game(socket):
    board = create_board()
    place_ships(board)

    while True:
        # Receive opponent's move
        opponent_move = receive_message(socket)
        row, col = map(int, opponent_move.split(','))

        if board[row][col] == 'S':
            board[row][col] = 'X'
            send_message(socket, 'Hit')
        else:
            board[row][col] = 'M'
            send_message(socket, 'Miss')

        print_board(board)

        # Check for win condition
        if all(cell == 'X' or cell == 'M' for row in board for cell in row):
            print("You lose!")
            break

        # Make your move
        while True:
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter column (0-9): "))
            if 0 <= row <= 9 and 0 <= col <= 9:
                break
        send_message(socket, f"{row},{col}")

        # Receive result of your move
        result = receive_message(socket)
        if result == 'Hit':
            print("You hit!")
        else:
            print("You missed!")

        # Check for win condition
        if all(cell == 'X' or cell == 'M' for row in board for cell in row):
            print("You win!")
            break

if __name__ == "__main__":
    client_socket = create_connection()
    play_game(client_socket)
    client_socket.close()

"""ex. 7: online-calculator"""
# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

while True:
    conn, addr = server.accept()
    expression = conn.recv(1024).decode('utf-8')
    try:
        result = eval(expression)
        conn.send(str(result).encode('utf-8'))
    except Exception as e:
        conn.send(f"Error: {e}".encode('utf-8'))
    conn.close()

# client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

expression = input("Enter an expression to calculate: ")
client.send(expression.encode('utf-8'))

result = client.recv(1024).decode('utf-8')
print("Result:", result)
client.close()

"""ex. 8: authorization to server"""
# server
import socket
import hashlib

def hash_password(username, password):
    return hashlib.sha256((username + ':' + password).encode()).hexdigest()

def check_user(username, password):
    with open('users.txt', 'r') as f:
        for line in f:
            hashed_pw = line.strip()
            if hash_password(username, password) == hashed_pw:
                return True
        return False

def register_user(username, password):
    with open('users.txt', 'a') as f:
        f.write(hash_password(username, password) + '\n')

def server_loop():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        data = client_socket.recv(1024).decode()
        username, password, action = data.split(':')

        if action == 'login':
            if check_user(username, password):
                client_socket.sendall('success'.encode())
            else:
                client_socket.sendall('failure'.encode())
        elif action == 'register':
            register_user(username, password)
            client_socket.sendall('registered'.encode())

if __name__ == '__main__':
    server_loop()

# client
import socket
import tkinter as tk
import hashlib

def login_attempt():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256((username + ':' + password).encode()).hexdigest()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    client_socket.sendall(f"{username}:{hashed_password}:login".encode())

    response = client_socket.recv(1024).decode()
    if response == 'success':
        # Open the main application window
        main_window = tk.Tk()
        # ... (main window setup)
        main_window.mainloop()
    else:
        error_label.config(text="Invalid username or password")

def register_attempt():
    # ... (similar to login_attempt, but sends 'register' action)
    
    # ... (Tkinter GUI setup for login and registration forms)

    """ex. 9: hex, etc. online"""
# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode('utf-8')
    number, base = map(int, data.split())
    result = format(number, 'b' if base == 2 else 'o' if base == 8 else 'x')
    conn.send(result.encode('utf-8'))
    conn.close()

# client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

number = input("Input a variable: ")
base = input("Enter the base (2, 8 or 16)): ")
client.send(f"{number} {base}".encode('utf-8'))

result = client.recv(1024).decode('utf-8')
print("Result:", result)
client.close()


"""ex. 10: Solving quadratic equations"""
# server
import socket
import math

def solve_quadratic(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return "No real roots"
    elif d == 0:
        x = -b / (2 * a)
        return f"Single root: {x}"
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Two roots: {x1}, {x2}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode('utf-8')
    a, b, c = map(int, data.split())
    result = solve_quadratic(a, b, c)
    conn.send(result.encode('utf-8'))
    conn.close()

# result
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

a = input("Enter the coefficient a: ")
b = input("Enter the coefficient b: ")
c = input("Enter the coefficient c: ")

client.send(f"{a} {b} {c}".encode('utf-8'))

result = client.recv(1024).decode('utf-8')
print("Result:", result)
client.close()