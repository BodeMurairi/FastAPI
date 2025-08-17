#!/usr/bin/env python3

import asyncio
import time

def qu():
    print("Why can't programmers tell jokes?")
    time.sleep(3)

def an():
    print("Timing!")

def test():
    qu()
    an()

async def q():
    print("Why can't programmers tell jokes?")
    await asyncio.sleep(3)

async def a():
    print("Timing!")

async def main():
    await asyncio.gather(q(), a())


# running synchronous main
if __name__ == "__main__":
    print("running sync main")
    print("________________")
    test()
    print("________________")
    print("running async main")
    asyncio.run(main())
