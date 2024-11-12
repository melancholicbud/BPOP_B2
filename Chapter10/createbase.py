import os
import sqlite3

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    db_is_created = os.path.exists(db_name)
    connection = sqlite3.connect(db_name)
    if db_is_created:
        print('Connection to existed database!')
    else:
        ("Creating a new database! You need definition data-scheme")
        