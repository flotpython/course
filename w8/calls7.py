import asyncio

async def coro():
    print("dans coro")

async def amain():
    # pareil mais depuis
    # une coroutine
    coro()

asyncio.get_event_loop().\
   run_until_complete(amain())
