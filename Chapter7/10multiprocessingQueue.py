from multiprocessing import Process, Queue

def pow_square(value, queue):
    for i in value:
        queue.put(i*i)
    
def pow_cube(value, queue):
    for i in value:
        queue.put(i*i*i)

if __name__ == "__main__":
    my_numbers = range(3)

    queue = Queue()
    process_pow_square = Process(target=pow_square,
                                 args=(my_numbers, queue),)
    process_pow_cube = Process(target=pow_cube,
                               args=(my_numbers, queue),)
    process_pow_square.start()
    process_pow_cube.start()

    process_pow_square.join()
    # waiting for closing a process
    process_pow_cube.join()

    while not queue.empty():
        print(queue.get(), end=" ")