import asyncio

async def coro():
    print("dans coro")

async def main():
    # pareil mais depuis une coroutine
    coro()

asyncio.ensure_future(main())
asyncio.get_event_loop().run_forever()
