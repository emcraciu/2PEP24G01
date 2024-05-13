import asyncio

import aiohttp


async def get_time(regions: list):
    async with aiohttp.ClientSession() as session:
        for region in regions:
            response = await session.request(
                method="GET",
                url=f"https://worldtimeapi.org/api/timezone/America/Boisehttps://worldtimeapi.org/api/timezone/{region}")
            print(response.text)


async def main():
    task = await asyncio.gather(
        get_time(["America/New_York", "Europe/Zurich"]),
        get_time(["Europe/Tallinn", "Pacific/Fiji"]),
    )
    print(task)


if __name__ == "__main__":
    asyncio.run(main())


