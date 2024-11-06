import asyncio
async def test_async():
    print(await func())

async def func():
    return "Hello, async world!"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_async())

@asyncio.coroutines
def test_async():
    print((yield from func()))

@asyncio.coroutines
def func():
    return "Hello, async world!"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_async())

async def first_function():
    print("first_function start")
    for it in range(7):
        await asyncio.sleep(1.2)
        print(f"first_function {it}")

async def second_function(): 
    print("second_function start") 
    for it in range(10):
        await asyncio.sleep(0.9)
        print(f"second_function {it}")
if __name__ == "__main__":
    loop = asyncio.get_event_loop() 
    my_functions = asyncio.wait( [first_function(), second_function()]) 
    loop.run_until_complete(my_functions)