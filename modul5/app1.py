# get timezone from each continents


import aiohttp

import asyncio

"https://worldtimeapi.org/api/timezone"

zones = ["Africa", "America", "Antarctica"]


async def get_time_zone_continent(continent: str):
    async with aiohttp.ClientSession() as session:
        response = await session.request(
            method="GET",
            url=f"https://worldtimeapi.org/api/timezone/{continent}"
        )
        print(await response.text())


async def main():
    task = await asyncio.gather(
        *(get_time_zone_continent(location) for location in zones)
    )


if __name__ == "__main__":
    asyncio.run(main())
