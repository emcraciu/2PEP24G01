import asyncio
import json
import aiohttp


async def get_time(regions: list):
    async with aiohttp.ClientSession() as session:
        responses = []
        for region in regions:
            response = await session.request(
                method="GET",
                url=f"https://worldtimeapi.org/api/timezone/{region}")
            responses.append(response)
        for response in responses:
            result = await response.text()
            print(result)


async def main():
    task = await asyncio.gather(
        get_time(["America/New_York", "Europe/Zurich"]),
        get_time(["Europe/Tallinn", "Pacific/Fiji"]),
    )
    print(task)


if __name__ == "__main__":
    asyncio.run(main())


