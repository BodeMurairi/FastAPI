#!/usr/bin/env python3

import asyncio

asyncio def set_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"set the future result to {value}")

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(set_future_result(future, "Future is ready"))

    result = await future
    print(f"Received future: {result}")

asyncio.run(main())
