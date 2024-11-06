from multiprocessing import Process

def process_run(num):
    print(f"Process # {num}")

if __name__ == "__main__":
    for it in range(5):
        my_process = Process(target=process_run,
                             args=(it,))
        my_process.start()