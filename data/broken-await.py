import asyncio

async def hello_world():
    await asyncio.sleep(0.2)
    print("Hello World")

# ceci ne fonctionne pas en Python standard
await hello_world()
