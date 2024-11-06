from threading import Thread, Event
import logging
import time

def event_work(event):
    logging.debug("run event_work")
    event_wait = event.wait()
    logging.debug("Flag is placed")

def event_with_timeout(event, time):
    while not event.is_set(): # is flag placed?
        logging.debug(f"Waiting for placing a flag or ETA in event_with_timeout")
        event_wait = event.wait(time)
        logging("Flag is placed")
        if event_wait:
            logging.debug("Processing event")
        else:
            logging.debug("Flag wasn't placed")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadname)-10s) $(message)s',
    )
    event = Event()
    my_thread1 = Thread(name='event_thread',
                        target=event_work,
                        args=(event,))
    my_thread1.start()
    my_thread2 = Thread(name='event_timeout',
                        target=event_with_timeout,
                        args=(event, 3))
    my_thread2.start()
    logging.debug('Latency before placing a flag')
    time.sleep(0.3)
    event.set()
    logging.debug("Flag is placed")