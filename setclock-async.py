import asyncio
from setclock_code import time_read

async def time_from_usb():
    time_reader = TimeReader(verbose=False)
    while True:
        time_reader.poll()
        await asyncio.sleep(0.2)

asyncio.create_task(time_from_usb())

if __name__ == "__main__":
    asyncio.get_event_loop().run_forever()
