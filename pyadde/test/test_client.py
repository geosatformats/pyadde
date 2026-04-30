from pyadde.client import AddeClient


async def run(host:str):
    async with AddeClient(host=host, user='DAS', project=6999) as c:
        print(c.json_content())

if __name__ == '__main__':
    import asyncio
    asyncio.run(run(host='snpp.ssec.wisc.edu'))
