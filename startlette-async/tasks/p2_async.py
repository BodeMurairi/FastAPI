#!/usr/bin/env python3
import asyncio

# coroutine func
async def fetch_data(id, delay):
    print(f"Coroutine with id {id} starting to fecth data")
    await asyncio.sleep(delay)
    return {"id": id,"data": f"Sample data from coroutine with id: {id}"}

async def main():
    results = await asyncio.gather(fetch_data(id=1, delay=2),
                                  fetch_data(id=2, delay=3),
                                  fetch_data(id=3, delay=1))
  
    # process the result
    for result in results:
        print(f"Received result: {result}")

# run main
asyncio.run(main())