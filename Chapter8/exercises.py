"""ex. 1: calculator"""
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by 0!")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print("Add: ", calc.add(5, 2))
    print("Subtract: ", calc.subtract(5, 2))
    print("Multiply: ", calc.multiply(5, 2))
    print("Divide: ", calc.divide(5, 2))


"""ex. 2: To-Do List"""
import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.tasks = json.load(f)

if __name__ == "__main__":
    todo = ToDoList()
    todo.add_task("Go to shop")
    todo.add_task("Make a homework")
    todo.save_to_file("tasks.json")
    todo.load_from_file("tasks.json")
    print("Tasks: ", todo.tasks)

"""ex. 3: list of a directory"""
import os

def list_directory(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print("Directory not found.")

if __name__ == "__main__":
    directory = input("Input path: ")
    list_directory(directory)


"""ex. 4: TicTacToe"""
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind, col_ind = square // 3, square % 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        col = [self.board[col_ind + i * 3] for i in range(3)]
        diag1 = [self.board[i] for i in (0, 4, 8)]
        diag2 = [self.board[i] for i in (2, 4, 6)]
        lines = [row, col, diag1, diag2]
        return any(all(spot == letter for spot in line) for line in lines)

    def is_board_full(self):
        return ' ' not in self.board

    def play(self):
        letter = 'X'
        while True:
            self.print_board()
            square = int(input(f"Player {letter}'s turn. Enter a square (0-8): "))
            if self.make_move(square, letter):
                if self.current_winner:
                    print(f"Player {letter} wins!")
                    break
                if self.is_board_full():
                    print("It's a tie!")
                    break
            letter = 'O' if letter == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

"""ex. 5: Write a program to view images in a given directory."""
import os
from PIL import Image

def view_images_in_directory(directory_path):
    """
    Views images in a given directory.

    Args:
        directory_path (str): Path to the directory containing images.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(directory_path, filename)
            image = Image.open(image_path)
            image.show()

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    view_images_in_directory(directory_path)

"""ex. 6: solve_quadratic"""
import cmath

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    sol1 = (-b + cmath.sqrt(d)) / (2*a)
    sol2 = (-b - cmath.sqrt(d)) / (2*a)
    return sol1, sol2

if __name__ == "__main__":
    a, b, c = map(float, input("Input coefs a, b и c: ").split())
    solutions = solve_quadratic(a, b, c)
    print("Solution: ", solutions)

"""ex. 7: Write a program that allows you to create new text files, 
populate them, save, load and edit them, and search the text."""
import os

def create_file(filename):
    with open(filename, 'w') as file:
        file.write('')
    print(f"File '{filename}' created successfully.")

def populate_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')
    print(f"Content added to '{filename}'.")

def save_file(filename):
    # No need to save explicitly if the file is open in write mode
    print(f"File '{filename}' saved.")

def load_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def edit_file(filename):
    try:
        with open(filename, 'r+') as file:
            content = file.read()
            print(content)
            new_content = input("Enter new content (or leave blank to keep original): ")
            if new_content:
                file.seek(0)
                file.write(new_content)
                file.truncate()
            print(f"File '{filename}' edited successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def search_text(filename, search_term):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if search_term in content:
                print(f"Search term '{search_term}' found in '{filename}'.")
            else:
                print(f"Search term '{search_term}' not found in '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Create a new file")
        print("2. Populate a file")
        print("3. Save a file")
        print("4. Load a file")
        print("5. Edit a file")
        print("6. Search text in a file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the filename: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Enter the filename: ")
            content = input("Enter the content: ")
            populate_file(filename, content)
        elif choice == '3':
            filename = input("Enter the filename: ")
            save_file(filename)
        elif choice == '4':
            filename = input("Enter the filename: ")
            load_file(filename)
        elif choice == '5':
            filename = input("Enter the filename: ")
            edit_file(filename)
        elif choice == '6':
            filename = input("Enter the filename: ")
            search_term = input("Enter the search term: ")
            search_text(filename, search_term)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""ex. 8: write a program that implements directory functionality with 
the ability to save, load, edit data, and search by last name"""
import json

class Directory:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new one.")

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_entry(self, first_name, last_name, phone_number, email):
        self.data.append({
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email
        })

    def edit_entry(self, last_name):
        for entry in self.data:
            if entry["last_name"] == last_name:
                print("Found entry:")
                print(entry)
                first_name = input("Enter new first name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                entry["first_name"] = first_name
                entry["phone_number"] = phone_number
                entry["email"] = email
                print("Entry updated successfully.")
                return
        print("Entry not found.")

    def delete_entry(self, last_name):
        for i, entry in enumerate(self.data):
            if entry["last_name"] == last_name:
                del self.data[i]
                print("Entry deleted successfully.")
                return
        print("Entry not found.")

    def search_by_last_name(self, last_name):
        results = [entry for entry in self.data if entry["last_name"] == last_name]
        if results:
            for entry in results:
                print(entry)
        else:
            print("No entries found for the given last name.")

    def display_all_entries(self):
        for entry in self.data:
            print(entry)

def main():
    directory = Directory("directory.json")
    directory.load_data()

    while True:
        print("\nDirectory Menu:")
        print("1. Add Entry")
        print("2. Edit Entry")
        print("3. Delete Entry")
        print("4. Search by Last Name")
        print("5. Display All Entries")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            directory.add_entry(first_name, last_name, phone_number, email)
        elif choice == '2':
            last_name = input("Enter last name to edit: ")
            directory.edit_entry(last_name)
        elif choice == '3':
            last_name = input("Enter last name to delete: ")
            directory.delete_entry(last_name)
        elif choice == '4':
            last_name = input("Enter last name to search: ")
            directory.search_by_last_name(last_name)
        elif choice == '5':
            directory.display_all_entries()
        elif choice == '6':
            directory.save_data()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""ex. 9: write a program that searches for files by name 
or part of a name in a user-defined directory"""
import os

def search_files(directory, search_term):
    """
    Searches for files in a directory and its subdirectories based on the search term.

    Args:
        directory (str): The root directory to search.
        search_term (str): The term to search for in filenames.

    Returns:
        list: A list of file paths that match the search term.
    """

    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if search_term.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

if __name__ == "__main__":
    directory_path = input("Enter the directory path to search: ")
    search_term = input("Enter the search term: ")

    results = search_files(directory_path, search_term)

    if results:
        print("Found files:")
        for file in results:
            print(file)
    else:
        print("No files found matching the search term.")

"""ex. 10: write a program that allows only authorized users to enter its main window,
with the possibility of registering a new user. The hash of the user's 'login:password' 
mapping is stored in a separate file"""
import hashlib
import json

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    hashed_password = hashlib.sha256((username + ":" + password).encode()).hexdigest()
    
    with open("users.json", "r+") as f:
        users = json.load(f)
        users[username] = hashed_password
        f.seek(0)
        json.dump(users, f, indent=4)
        f.truncate()
    
    print("User registered successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    hashed_password = hashlib.sha256((username + ":" + password).encode()).hexdigest()
    
    with open("users.json", "r") as f:
        users = json.load(f)
        
        if username in users and users[username] == hashed_password:
            print("Login successful!")
            # Here, you would typically open the main window or start the main program
        else:
            print("Invalid username or password.")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

"""ex. 11: Write a program that converts currencies, 
the list of which is taken from a json file with data 
on their current exchange rate."""
import json

def load_exchange_rates(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Currency not found.")

    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]

    converted_amount = amount * (to_rate / from_rate)
    return converted_amount

def main():
    exchange_rates_file = "exchange_rates.json"
    exchange_rates = load_exchange_rates(exchange_rates_file)

    while True:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency: ").upper()
        to_currency = input("Enter the target currency: ").upper()

        try:
            converted_amount = convert_currency(amount, 
                                                from_currency, to_currency, 
                                                exchange_rates)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        except ValueError as e:
            print(e)

        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()

"""ex. 12: Write a program to plot data from an MS Excel file. 
The file can contain any number of sheets, each of which stores values 
for abscissa and ordinate axes (2 columns per sheet in total). 
In the developed application it is necessary to switch between graphs using TabWidget."""
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotWindow(QMainWindow):
    def __init__(self, excel_file):
        super().__init__()
        self.setWindowTitle("Excel Data Plots")

        # Create a tab widget
        self.tabs = QTabWidget()

        # Read Excel data
        self.excel_data = pd.read_excel(excel_file, sheet_name=None)

        # Create plots for each sheet
        for sheet_name, df in self.excel_data.items():
            # Create a plot
            figure = Figure()
            ax = figure.add_subplot(111)
            ax.plot(df.iloc[:, 0], df.iloc[:, 1])
            ax.set_xlabel(df.columns[0])
            ax.set_ylabel(df.columns[1])
            ax.set_title(sheet_name)

            # Create a canvas to display the plot
            canvas = FigureCanvas(figure)

            # Create a widget to hold the canvas
            widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(canvas)
            widget.setLayout(layout)

            # Add the widget to the tab widget
            self.tabs.addTab(widget, sheet_name)

        # Set the tab widget as the central widget
        self.setCentralWidget(self.tabs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    excel_file = 'your_excel_file.xlsx'  # Replace with your Excel file path
    window = PlotWindow(excel_file)
    window.show()
    sys.exit(app.exec_())

"""ex. 13: Write a GUI program to graph 
the distances between objects 
and find the shortest path between given graph vertices."""
import sys
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.G = nx.Graph()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()

        # Input fields
        self.node_input = QLineEdit()
        self.edge_input1 = QLineEdit()
        self.edge_input2 = QLineEdit()
        self.edge_weight_input = QLineEdit()
        self.start_node_input = QLineEdit()
        self.end_node_input = QLineEdit()

        # Buttons
        self.add_node_button = QPushButton("Add Node")
        self.add_edge_button = QPushButton("Add Edge")
        self.find_path_button = QPushButton("Find Shortest Path")

        # Label for path display
        self.path_label = QLabel()

        # Matplotlib canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Layout setup
        layout.addWidget(self.node_input)
        layout.addWidget(self.add_node_button)
        layout.addWidget(self.edge_input1)
        layout.addWidget(self.edge_input2)
        layout.addWidget(self.edge_weight_input)
        layout.addWidget(self.add_edge_button)
        layout.addWidget(self.start_node_input)
        layout.addWidget(self.end_node_input)
        layout.addWidget(self.find_path_button)
        layout.addWidget(self.path_label)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        # Connect button clicks to functions
        self.add_node_button.clicked.connect(self.add_node)
        self.add_edge_button.clicked.connect(self.add_edge)
        self.find_path_button.clicked.connect(self.find_shortest_path)

    def add_node(self):
        node = self.node_input.text()
        self.G.add_node(node)
        self.update_plot()

    def add_edge(self):
        node1 = self.edge_input1.text()
        node2 = self.edge_input2.text()
        weight = int(self.edge_weight_input.text())
        self.G.add_edge(node1, node2, weight=weight)
        self.update_plot()

    def find_shortest_path(self):
        start_node = self.start_node_input.text()
        end_node = self.end_node_input.text()
        try:
            path = nx.shortest_path(self.G, source=start_node, target=end_node, weight='weight')
            self.path_label.setText(f"Shortest path: {path}")
        except nx.NetworkXNoPath:
            self.path_label.setText("Path not found")
        self.update_plot(highlight_path=path)

    def update_plot(self, highlight_path=None):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, ax=ax)
        nx.draw_networkx_edges(self.G, pos, ax=ax)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=nx.get_edge_attributes(self.G, 'weight'), ax=ax)

        if highlight_path:
            nx.draw_networkx_edges(self.G, pos, edgelist=[(path[i], path[i+1]) 
                                                          for i in range(len(path)-1)], width=2, color='red', ax=ax)

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GraphApp()
    ex.show()
    sys.exit(app.exec_())

"""ex. 14: Write a program to encrypt and decrypt a file using any algorithm you choose."""
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(filename + '.encrypted', 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename[:-10], 'wb') as f:
        f.write(decrypted_data)

if __name__ == '__main__':
    # Generate a key (only needed once)
    # generate_key()

    # Read the key
    with open('key.key', 'rb') as file:
        key = file.read()

    # Encrypt a file
    encrypt_file('your_file.txt', key)

    # Decrypt a file
    decrypt_file('your_file.txt.encrypted', key)

"""ex. 15: Write a program that allows you to generate a list 
with a choice of algorithm options for sorting it (at least 2 algorithms)."""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    while True:
        print("1. Bubble Sort")
        print("2. Quick Sort")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            bubble_sort(arr)
            print("Sorted array:", arr)
        elif choice == '2':
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            arr = quick_sort(arr)
            print("Sorted array:", arr)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""ex. 16: Write a program that randomly generates a password when a button is pressed."""
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Random password: ", generate_password())


"""ex. 17: Write a program to convert values 
to different number systems (decimal, octal, binary, hexadecimal)."""
def convert_base(num, base):
    """
    Converts a number to a specific base.

    Args:
        num (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The converted number as a string.
    """

    if num == 0:
        return '0'

    digits = '0123456789ABCDEF'
    result = ''

    while num > 0:
        digit = num % base
        result = digits[digit] + result
        num //= base

    return result

def main():
    while True:
        num = int(input("Enter a number: "))
        base = int(input("Enter the base to convert to (2, 8, 10, 16): "))

        if base not in [2, 8, 10, 16]:
            print("Invalid base. Please enter 2, 8, 10, or 16.")
            continue

        result = convert_base(num, base)
        print(f"The number {num} in base {base} is: {result}")

        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()

"""ex. 18: Write a program to view video files in a user-defined directory."""
import os
import cv2

def view_videos_in_directory(directory_path):
    """
    Views videos in a given directory.

    Args:
        directory_path (str): Path to the directory containing videos.
    """

    for filename in os.listdir(directory_path):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(directory_path, filename)
            cap = cv2.VideoCapture(video_path)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                cv2.imshow(filename, frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    view_videos_in_directory(directory_path)

"""ex. 19: Write a program that implements the basic functionality of Paint."""
import tkinter as tk
from tkinter import filedialog

class PaintApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Paint")
        self.geometry("500x500")

        self.canvas = tk.Canvas(self, width=480, height=480, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color = 'black'
        self.size = 2

        self.setup_toolbar()

    def setup_toolbar(self):
        toolbar = tk.Frame(self)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Color buttons
        red_button = tk.Button(toolbar, bg='red', width=2, command=lambda: self.set_color('red'))
        red_button.pack(side=tk.LEFT)
        green_button = tk.Button(toolbar, bg='green', width=2, command=lambda: self.set_color('green'))
        green_button.pack(side=tk.LEFT)
        blue_button = tk.Button(toolbar, bg='blue', width=2, command=lambda: self.set_color('blue'))
        blue_button.pack(side=tk.LEFT)
        black_button = tk.Button(toolbar, bg='black', width=2, command=lambda: self.set_color('black'))
        black_button.pack(side=tk.LEFT)

        # Size buttons
        small_button = tk.Button(toolbar, text='Small', command=lambda: self.set_size(2))
        small_button.pack(side=tk.LEFT)
        medium_button = tk.Button(toolbar, text='Medium', command=lambda: self.set_size(5))
        medium_button.pack(side=tk.LEFT)
        large_button = tk.Button(toolbar, text='Large', command=lambda: self.set_size(10))
        large_button.pack(side=tk.LEFT)

        # Clear button
        clear_button = tk.Button(toolbar, text='Clear', command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        # Save button
        save_button = tk.Button(toolbar, text='Save', command=self.save_canvas)
        save_button.pack(side=tk.LEFT)

    def set_color(self, color):
        self.color = color

    def set_size(self, size):
        self.size = size

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        self.canvas.postscript(file=file_path, colormode='color')

    def paint(self, event):
        x1, y1 = (event.x - self.size), (event.y - self.size)
        x2, y2 = (event.x + self.size), (event.y + self.size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def __init__(self):
        super().__init__()
        self.canvas.bind('<B1-Motion>', self.paint)

if __name__ == '__main__':
    app = PaintApp()
    app.mainloop()

"""ex. 20: Snake game"""
import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

display_width = 800
display_height = 600

block_size = 10

font_style = pygame.font.SysFont(None, 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width / 6, display_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [foodx, foody, block_size, block_size])
        pygame.draw.rect(gameDisplay, black, [x1, y1, block_size, block_size])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

        pygame.time.Clock().tick(20)

    pygame.quit()
    quit()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
gameLoop()