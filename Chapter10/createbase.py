import os
import sqlite3

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    db_schema_name = 'my_todolist_definition.sql'
    db_is_created = os.path.exists(db_name)
    connection = sqlite3.connect(db_name)
    if db_is_created:
        print('Connection to existed database!')
    else:
        ("Creating a new database! You need definition data-scheme")
    
    with open(db_schema_name, 'rt') as schema_file:
        my_schema = schema_file.read()
        # running a code of creating sheets 
        # uploaded from my_todolist_definition.sql
    connection.executescript(my_schema)

    print('Adding data in database!')
    connection.executescript('''
        insert into my_project(name, description, deadline)
        values ('MagicMonth', 'Learning a Python in 80 days', '2024-11-12')
    ''')
    connection.executescript('''
        insert into my_task(description, deadline, status, project)
        values ('Syntax & data structure', '2024-11-08', 'done', 'MagicMonth')
    ''')
    connection.executescript('''
        insert into my_task(description, deadline, status, project)
        values ('Crying, because it is not easy', '2024-11-30', 'wait', 'MagicMonth')
    ''')  
