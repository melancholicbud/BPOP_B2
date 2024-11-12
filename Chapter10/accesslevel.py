import sqlite3
import logging
from threading import Thread, Event
import time

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s (%(threadName)-10s) %(message)s',
)
db_name = 'my_todolist.db'

def writer_to_db(sync_event, level):
    with sqlite3.connect(db_name, isolation_level=level) as connection:
        cursor = connection.cursor()
        cursor.execute('update my_task set priority = priority+1')
        logging.debug("Waiting for synchs")
        sync_event.wait()
        logging.debug("Pause at work")
        time.sleep(1)
        connection.commit()
        logging.debug("Checking updates")

def reader_to_db(sync_event, level):
    with sqlite3.connect(db_name, isolation_level=level) as connection:
        cursor = connection.cursor()
        logging.debug("Waiting for synchs")
        sync_event.wait()
        logging.debug("Waiting")
        cursor.execute('select * from my_task')
        logging.debug("Table selection is done")
        cursor.fetchall()
        logging.debug("Getting a result")

if __name__ == "__main__":
    isolation_level = 'DEFERRED'
    # isolation_level = 'IMMEDIATE'
    # isolation_level = 'EXCLUSIVE'
    sync_event = Event()
    my_threads = [
        Thread(name='Jim Carrey',
               target=writer_to_db,
               args=(sync_event, isolation_level,)),
        Thread(name='Denzel Washington',
               target=writer_to_db,
               args=(sync_event, isolation_level,)),
        Thread(name='Jack Nicolson',
               target=reader_to_db,
               args=(sync_event, isolation_level,)),
        Thread(name='Cameron Dias',
               target=reader_to_db,
               args=(sync_event, isolation_level,)),
    ]
    [it.start() for it in my_threads]
    time.sleep(2)
    logging.debug("Preparation is done")
    sync_event.set()
    [it.join() for it in my_threads]