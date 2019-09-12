import re
import scrapy
from ..items import HouseItem


class HouseSpider(scrapy.Spider):
    name = 'houses'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
    }
    def start_requests(self):
        urls = ['https://cd.lianjia.com/zufang/pg{}rt200600000001/'.format(i) for i in range(1, 31)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        print(response.url)
        for i in response.css('div.content__list--item--main'):
            housing_estate = i.css('p.content__list--item--des a::attr(title)').extract_first().strip()
            area = i.css('p.content__list--item--des::text').re_first('(\d+)㎡')
            orientations = i.css('p.content__list--item--des::text').extract()[5].strip()
            apartment = i.css('p.content__list--item--des::text').extract()[6].strip()
            rent = i.css('span.content__list--item-price em::text').extract_first().strip()

            yield HouseItem(
                housing_estate = housing_estate,
                area = int(area),
                orientations = orientations,
                apartment = apartment,
                rent = int(rent)
            )
