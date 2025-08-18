#!/usr/bin/env python3
import asyncio

# coroutine func
async def fetch_data(id, delay):
    print(f"Coroutine with id {id} starting to fecth data")
    await asyncio.sleep(delay)
    return {"id": id,"data": f"Sample data from coroutine with id: {id}"}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"received result: {result}")

asyncio.run(main())
