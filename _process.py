import asyncio
import time
import multiprocessing
from typing import List
from multiprocessing.context import Process


def shout_worker(num: int):
    asyncio.run(_shout_worker(num))


async def _shout_worker(num: int):
    future_list = [_shout(num, i) for i in range(1000)]
    await asyncio.gather(*future_list)


async def _shout(num: int, i: int):
    await asyncio.sleep(0)
    print(f"프로세스 = {num}, 순서 = {i}")


async def _async_main():
    start = time.time()
    loop = asyncio.get_running_loop()

    future_list = [
        loop.run_in_executor(
            None,
            multiprocessing.Process,
            None,
            shout_worker,
            None,
            (i,)
        ) for i in range(100)
    ]

    process_list: List[Process] = await asyncio.gather(*future_list)

    future_list = [
        loop.run_in_executor(
            None,
            proc.start
        ) for proc in process_list
    ]

    try:
        await asyncio.gather(*future_list)

        for proc in process_list:
            proc.join()

    finally:
        end = time.time()
        print(end - start)


def main():
    asyncio.run(_async_main())


if __name__ == "__main__":
    main()
