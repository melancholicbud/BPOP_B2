from threading import Thread
import logging

class MyThread(Thread):
    def __init__(self, group=None, target=None,
                 name=None, args=(), kwargs=None,
                 *, daemon=True):
        super().__init__(group=group, target=target,
                         name=name, daemon=True)
        self.args = args
        self.kwargs = kwargs
    
    def run(self)->None:
        logging.debug(f'Thread args = {self.args} '
                      f'and kwargs = {self.kwargs}')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadname)-10s) %(message)s')
    
    for it in range(5):
        new_thread = MyThread(args=(it,),
                              kwargs={it: it+2, f"{it}": str(it)*2})
        new_thread.start()