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
    with sqlite3.connect(db_name) as connection:
        print("Starting state of DB")
        # output current projects
        all_project_show(connection)
        try:
            cursor = connection.cursor()
            cursor.execute("""delete from my_project where name = 'SuperProgrammer'""")
            print("State of DB after deleting a project")
            all_project_show(connection)
            raise RuntimeError("Error while deleting")
        except Exception as my_simulated_error:
            print("Rollback updates")
            connection.rollback()
        else:
            connection.commit()
        
        print("State of DB after rollback method")
        all_project_show(connection)