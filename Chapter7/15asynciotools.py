import asyncio
import functools

def callback(arg, kwarg='default'):
    print(f'Callback arg={arg}, kwarg = {kwarg}')

async def main(loop):
    print('Registration of a callback-function')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='^_^')
    loop.call_soon(wrapped, "-_-")
    await asyncio.sleep(0.2)

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        print("starting an event cycle")
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('Stopping a cycle')
        event_loop.close()