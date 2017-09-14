import asyncio

async def coro():
    # totalement légal
    print("dans coro")

def main():
    # par contre ici il
    # manque un await !
    coro()

main()    
