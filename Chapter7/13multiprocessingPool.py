from multiprocessing import Process, current_process, cpu_count, Pool

def square(data):
    return data * data

def start_process():
    print(f'Starting a process - {current_process().name}')

if __name__ == "__main__":
    inputs = list(range(10))
    print(f'Starting list: {inputs}')
    bultin_map = map(square, inputs)
    print(f'Embedded function map: {list(bultin_map)}')

    pool_size = cpu_count() * 2
    print(f'Amount of cores in processor: {cpu_count()}')
    print(f'Amount of pools: {pool_size}')
    pool = Pool(
        processes=pool_size,
        initializer=start_process,
    )
    pool_map = pool.map(square, inputs)
    pool.close()
    pool.join()
    print(f'Results of job in process pool: {pool_map}')