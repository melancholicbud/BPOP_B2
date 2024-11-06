import asyncio

async def task_test():
    print('Processing...')
    return(30, "-_-", [4.6, "o_O"])

async def main(loop):
    print('Declare a task!')
    task = loop.create_task(task_test())
    print(f'ETA: {task}')
    return_value = await task
    print(f'Getting done: {task}')
    print(f'Results: {return_value}')

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()