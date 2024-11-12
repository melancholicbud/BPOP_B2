"""ex. 1: TODO List"""
import sqlite3

def create_table():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}. {row[1]} {'(Completed)' if row[2] else ''}")
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def mark_complete(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def main():
    create_table()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_complete(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""ex. 2: electronic class journal"""
import sqlite3

def create_tables():
    conn = sqlite3.connect('class_journal.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            date DATE,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        )
    ''')

    conn.commit()
    conn.close()

# todo: done with adding, editing etc.

def main():
    create_tables()

    # Main loop for user interaction
    while True:
        print("\nElectronic Class Journal")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Add Grade")
        print("4. View Students")
        print("5. View Subjects")
        print("6. View Grades")
        print("7. Edit Student")
        print("8. Edit Subject")
        print("9. Edit Grade")
        print("10. Delete Student")
        print("11. Delete Subject")
        print("12. Delete Grade")
        print("13. Quit")

        choice = input("Enter your choice: ")

        # todo: implement the corresponding function for each choice

if __name__ == "__main__":
    main()


"""ex. 3: library electronic catalog"""
import sqlite3
from datetime import datetime, timedelta

def create_tables():
    conn = sqlite3.connect('library.db')
    cursor = conn.conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            genre TEXT,
            isbn TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT,
            phone_number TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            loan_date DATE,
            due_date DATE,
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES books(book_id),
            FOREIGN KEY (member_id) REFERENCES members(member_id)
        )
    ''')

    conn.commit()
    conn.close()

# todo: functions for adding, editing, deleting books etc.

def main():
    create_tables()

    # Main loop for user interaction
    while True:
        print("\nLibrary Electronic Catalog")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Loan Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Edit Book")
        print("9. Edit Member")
        print("10. Delete Book")
        print("11. Delete Member")
        print("12. Quit")

        choice = input("Enter your choice: ")

        # todo: implementing

if __name__ == "__main__":
    main()

"""amd many more the same exercises."""