from threading import Timer
import logging
import time

def thread_work():
    logging.debug("Okaaay, let's go!")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadname)-10s) %(message)s',
    )
    my_timer1 = Timer(0.3, thread_work)
    my_timer1.setName("MyThreadTimer-1")
    my_timer2 = Timer(0.3, thread_work)
    my_timer2.setName("MyThreadTimer-2")

    logging.debug("Starting a timers")
    my_timer1.start()
    my_timer2.start()

    logging.debug(f"Latency before cancellation {my_timer2.getName()}")
    time.sleep(0.2)
    logging.debug(f"Cancellation of thread - {my_timer2.getName()}")
    my_timer2.cancel()
    logging.debug("Finishing...")