import asyncio

async def my_coroutine():
    print("simple co-routine")

def main():

    loop = asyncio.get_event_loop()

    loop.run_until_complete(my_coroutine())

    loop.close()

main()