import requests as req
import asyncio
import aiohttp
import sys
import utils

# ****** UPDATE BEFORE USING ******
API_KEY = "YOUR_API_KEY"


async def build_insights(lines):
    for line in lines:
        print(line.strip())
    print(f"Sending requests for these websites to PageSpeed Insights API......\n")
    async with aiohttp.ClientSession() as session:
        mobile_task_list = []
        desktop_task_list = []
        for line in lines:
            url = line.strip()
            mobile_pagespeed_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key={API_KEY}&url={url}&strategy=mobile"
            desktop_pagespeed_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key={API_KEY}&url={url}&strategy=desktop"
            mobile_task = asyncio.ensure_future(
                get_insight_data(session, mobile_pagespeed_url))
            mobile_task_list.append(mobile_task)
            desktop_task = asyncio.ensure_future(
                get_insight_data(session, desktop_pagespeed_url))
            desktop_task_list.append(desktop_task)
        mobile_data = await asyncio.gather(*mobile_task_list)
        desktop_data = await asyncio.gather(*desktop_task_list)

    for i in range(0, len(lines)):
        url = lines[i].strip()
        result_file = open(f"./results/{url.split('.')[1]}.html", "w")
        result_file.write(utils.write_result_html(
            url, mobile_data[i], desktop_data[i]))
        result_file.close()
        print(f"Results built for {url}")
    print("Output can be found in results directory")


async def get_insight_data(session, url):
    async with session.get(url) as response:
        data = await response.json()
        response.close()
        return data


if __name__ == "__main__":
    # Filepath passed in as command line argument
    if len(sys.argv) != 2:
        raise Exception("Please include file path as argument")

    # read file of URLs into an array
    file_path = sys.argv[1]
    file_obj = open(file_path, "r")
    lines = file_obj.readlines()
    file_obj.close()

    # Call PageSpeed API and write to HTML result file
    print(f"\n---------- PageSpeed batch analysis starting ----------\n")
    # Uncomment line below for Windows
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(build_insights(lines))
    print(f"\n---------- PageSpeed batch analysis completed ----------\n")
