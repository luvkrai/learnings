import asyncio

async def some_old_function(data):
    print("Starting with {}".format(data))
    for i in range(data):
        pass
        if i%100000 == 0:
            await asyncio.sleep(.000000001)
    print("Done with {}".format(data))
		   
async def main():
    print("Starting with main")
    t1 = loop.create_task(some_old_function(100))
    t2 = loop.create_task(some_old_function(100000))
    t3 = loop.create_task(some_old_function(50000000))
    await asyncio.wait([t1,t2,t3])
    print("Done with main")
	

if __name__ == '__main__':
    print("start")
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        pass
    finally:
        loop.close()
