from threading import Thread, Condition
import logging
import time

def event_work(condition):
    logging.debug("run thread")
    with condition:
        condition.wait() # waiting for unblocking of resource
        logging.debug('Unblocked!')

def event_master(condition):
    logging.debug('Starting...')
    with condition:
        logging.debug('Unblocking!')
        condition.notifyAll()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadname)-3s) $(message)s',
    )
    condition = Condition()
    my_thread1 = Thread(name='event_thread1',
                        target=event_work,
                        args=(condition,))
    my_thread1.start()
    my_thread2 = Thread(name='event_thread2',
                        target=event_work,
                        args=(condition, ))
    event_master = Thread(name='master', 
                          target=event_master, 
                          args=(condition,))
    my_thread1.start()
    time.sleep(0.1)
    my_thread2.start()
    time.sleep(0.1)
    event_master.start()