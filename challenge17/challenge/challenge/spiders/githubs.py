import scrapy
from challenge.items import ChallengeItem

class GithubsSpider(scrapy.Spider):
    name = 'shiyanlou-github'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for github in response.css('div#user-repositories-list li'):
            item = ChallengeItem(
                name = github.css('h3 a::text').extract_first().strip(),
                update_time = github.css('relative-time ::attr(datetime)').extract_first().strip()
            )
            github_url = github.css('a::attr(href)').extract_first()
            full_github_url = response.urljoin(github_url)
            request = scrapy.Request(full_github_url, self.parse_others)
            request.meta['item'] = item
            yield request
        for url in response.css('div.paginate-container a::attr(href)'):
            yield response.follow(url, callback=self.parse)

    def parse_others(self, response):
        item = response.meta['item']
        item['commits'] = response.css('ul.numbers-summary a span::text').extract()[0]
        item['branches'] = response.css('ul.numbers-summary a span::text').extract()[1]
        item['releases'] = response.css('ul.numbers-summary a span::text').extract()[2]  
        yield item

