import asyncio
import aiohttp

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print(", world!")

asyncio.run(say_hello())

async def task(name, seconds):
    print(f"Task {name} starting...")
    await asyncio.sleep(seconds)
    print(f"Task {name} finished.")

async def main():
    await asyncio.gather(
        task("Task 1", 1),
        task("Task 2", 2),
        task("Task 3", 3),
    )

# asyncio.run 会创建一个事件循环
# aysncio.gather() 返回一个等待所有子协程完成的 Future
# 然后创建 Task 将任务都添加到事件循环中
# 接着顺序执行 Task，当遇到 await 时，则挂起协程
asyncio.run(main())

async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i
    
async def main():
    async for item in async_generator():
        print(item)

asyncio.run(main())

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)
        for page in pages:
            print(page[:100])       # 打印前100

asyncio.run(main())

async def fetch(session, url):
    async with session.get(url) as response:
        content = await response.read()
        return len(content)

async def fetch_all_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        lengths = await asyncio.gather(*tasks)
        return lengths

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3'
]

lengths = asyncio.run(fetch_all_pages(urls))
print(lengths) 