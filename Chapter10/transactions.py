import sqlite3

def all_project_show(connection):
    cursor = connection.cursor()
    cursor.execute('select name, description, deadline from my_project')
    print("Projects in the list: ")
    for name, description, deadline in cursor.fetchall():
        print("------------------------------")
        print(f' Name of project: "{name}" \n'
              f' Description: "{description}" \n'
              f' Deadline: {deadline}')
        print("------------------------------")

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    with sqlite3.connect(db_name) as first_connection:
        first_cursor = first_connection.cursor()
        print("Starting state of DB")
        # output current projects
        all_project_show(first_connection)
        
        first_cursor.execute('''
            insert into my_project(name, description, deadline)
                    values ('SuperProg', 'After learning Python getting a job after 30 days',
                             '2025-01-31')''')
        print('State of DB after updating')
        all_project_show(first_connection)
    
    print("State of DB before commit method")
    with sqlite3.connect(db_name) as second_connection:
        # output current projects
        all_project_show(second_connection)
        
    first_connection.commit()
    print("State of DB after commit method")
    with sqlite3.connect(db_name) as third_connection:
        # output current projects
        all_project_show(third_connection)