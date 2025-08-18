#!/usr/bin/env python3

import asyncio

# coroutine func
async def fetch_data(id, delay):
    print(f"Coroutine with id {id} starting to fecth data")
    await asyncio.sleep(delay)
    return {"id": id,"data": f"Sample data from coroutine with id: {id}"}

async def main():
    task1 = asyncio.create_task(fetch_data(id=1, delay=2))
    task2 = asyncio.create_task(fetch_data(id=2, delay=3))
    task3 = asyncio.create_task(fetch_data(id=3, delay=1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(f"Result: {result1} {result2} {result3}")

# run main coroutine
asyncio.run(main())
