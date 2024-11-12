import sqlite3

db_name = 'my_todolist.db'
with sqlite3.connect(db_name) as connection:
    cursor = connection.cursor()
    cursor.execute("""
        select id, priority, description,
                   status, deadline from my_task
                   where project = 'MagicMonth'
    """)
    # execute a data
    for it_row in cursor.fetchall():
        id, priority, description, status, deadline = it_row
        print(f"{id}, {priority}, {description}, {status}, {deadline}")