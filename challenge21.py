import csv
import asyncio
import aiohttp
import async_timeout
from scrapy.http import HtmlResponse

results = []

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

def parse(url, body):
    response = HtmlResponse(url=url, body=body)
    for repository in response.css('div#user-repositories-list li'):
        name = repository.css('h3 a::text').extract_first().strip()
        update_time = repository.css('relative-time ::attr(datetime)').extract_first().strip()
        results.append((name, update_time))

async def task(url):
    async with aiohttp.ClientSession() as session:
        the_body = await fetch(session, url)
        parse(url, the_body.encode('utf-8'))

def main():
    loop = asyncio.get_event_loop()
    url_list = ['https://github.com/shiyanlou?tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxNzozNjoxNSswODowMM4FkpW2&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yM1QxNDoxODoyMSswODowMM4By2VI&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0xOVQxMDoxMDoyMyswODowMM4BmcsV&tab=repositories'
    ]
    tasks = [task(url) for url in url_list]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()
