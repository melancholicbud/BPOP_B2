"""ex. 1: reading data from a file in one thread and writing it in another thread to another file"""
import threading

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def main():
    data = read_file("input.txt")

    write_thread = threading.Thread(target=write_file, args=("output.txt"))
    write_thread.start()
    write_thread.join()

if __name__ == "__main__":
    main()

"""ex. 2: Read data in one process and write data in another process"""
from multiprocessing import Process, Pipe
def read_file(filename, conn):
    with open(filename, 'r') as file:
        data = file.read()
    conn.send(data) # sending a data in another process
    conn.close()

def write_file(filename, conn):
    data = conn.recv() # getting a data from first process
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    reader = Process(target=read_file, args=("input.txt", child_conn))
    writer = Process(target=write_file, args=("output.txt", parent_conn))

    reader.start()
    writer.start()

    reader.join()
    writer.join()

"""ex. 3: asynchronous reading and writing files"""
import aiofiles
import asyncio

async def read_file(filename):
    async with aiofiles.open(filename, 'r') as file:
        return await file.read()
    
async def write_file(filename, data):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(data)

async def main():
    data = await read_file("input.txt")
    await write_file("output.txt", data)

if __name__ == "__main__":
    asyncio.run(main())

"""ex. 4: multiplication of two matrices using streams"""
def multiply_row(row, matrix, result, row_index):
    result[row_index] = [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)]

def matrix_multiply(matrix_a, matrix_b):
    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    threads = []

    for i, row in enumerate(matrix_a):
        thread = threading.Thread(target=multiply_row, args=(row, matrix_b, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    return result

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = matrix_multiply(matrix_a, matrix_b)
print(result)

"""ex. 5: Increasing the total meter by several processes"""
from multiprocessing import Process, Value, Lock

def increment(counter, lock):
    with lock:
        for _ in range(1000):
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0) # general counter
    lock = Lock() # protection against simultaneous access
    processes = [Process(target=increment, args=(counter, lock)) for _ in range(10)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Final counter value: ", counter.value)

"""ex. 6: The task of lunchtime philosophers (using processes)
   In the task of dining philosophers, the philosophers share forks, 
   and everyone can only eat if they have both forks on their sides. 
   The implementation uses Semaphore for access control."""
from multiprocessing import Process, Semaphore
import time
import random

def philosopher(philosopher_num, left_fork, right_fork):
    while True:
        print(f"Philosopher {philosopher_num} is thinking")
        time.sleep(random.uniform(0.1, 0.5))
        with left_fork:
            with right_fork:
                print(f"Philosopher {philosopher_num} is eating")
                time.sleep(random.uniform(0.1, 0.3))
                print(f"Philosopher {philosopher_num} is done eating")

if __name__ == "__main__":
    forks = [Semaphore(1) for _ in range(5)]
    philosophers = [Process(target=philosopher, 
                            args=(i, forks[i], forks[(i + 1) % 5])) 
                            for i in range(5)]
    
    for p in philosophers:
        p.start()
    
    for p in philosophers:
        p.join()

"""ex. 7: Filling lists with random values and finding the median in individual trials"""
from multiprocessing import Process
import random
import statistics

def calculate_median(numbers, index):
    median = statistics.median(numbers)
    print(f"Median for a list {index}: {median}")

if __name__ == "__main__":
    lists = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
    processes = []

    for i, lst in enumerate(lists):
        p = Process(target=calculate_median, args=(lst, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

"""ex. 8: Filling the queue with random values and retrieval in threads with identification"""
from multiprocessing import Process, Queue
import random
import time

def worker(q, worker_id):
    while not q.empty():
        value = q.get()
        print(f"The process {worker_id} ejected a value: {value}")
        time.sleep(0.1)

if __name__ == "__main__":
    q = Queue()
    for _ in range(20):
        q.put(random.randint(1, 100))

    processes = [Process(target=worker, args=(q, i)) for i in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

"""ex. 9: A counter that is alternately incremented by processes"""
from multiprocessing import Process, Value, Condition
import time

def increment(counter, condition, process_id):
    with condition:
        while counter.value < 50:
            condition.wait()  # waiting for the other thread to increase
            if counter.value < 50:
                counter.value += 5
                print(f"The process {process_id} increased a value to {counter.value}")
                condition.notify_all()  # report to another thread

if __name__ == "__main__":
    counter = Value('i', 0)
    condition = Condition()

    process1 = Process(target=increment, args=(counter, condition, 1))
    process2 = Process(target=increment, args=(counter, condition, 2))

    process1.start()
    process2.start()

    with condition:
        condition.notify_all()  # Starting a job

    process1.join()
    process2.join()

"""ex. 10: Reading data from a file and writing to three other files"""
from multiprocessing import Process, Queue
import time

def read_file(queue, filename):
    with open(filename, 'r') as file:
        for line in file:
            queue.put(line.strip())
    queue.put(None)  # Marking the end of reading

def write_file(queue, filename):
    while True:
        line = queue.get()
        if line is None:  # If reading is completed
            break
        with open(filename, 'a') as file:
            file.write(line + '\n')
            print(f"Filed{filename}: {line}")
        time.sleep(0.1)

if __name__ == "__main__":
    queue = Queue()
    
    reader_process = Process(target=read_file, args=(queue, "input.txt"))
    writer1_process = Process(target=write_file, args=(queue, "output1.txt"))
    writer2_process = Process(target=write_file, args=(queue, "output2.txt"))
    writer3_process = Process(target=write_file, args=(queue, "output3.txt"))

    reader_process.start()
    writer1_process.start()
    writer2_process.start()
    writer3_process.start()

    reader_process.join()
    queue.put(None)  # Complete the remaining processes
