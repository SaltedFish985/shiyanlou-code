import scrapy
from ..items import RestaurantItem


class RestaurantSpider(scrapy.Spider):
    name = 'restaurants'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
    }
    def start_requests(self):
        urls = ['https://bj.nuomi.com/326-page{}/'.format(i) for i in range(1, 31)]
        for url in urls:
            yield scrapy.Request(url=url, meta={ 'dont_redirect': True, 'handle_httpstatus_list': [302]}, callback=self.parse, headers=self.headers)

    def parse(self, response):
        print(response.url)
        for i in response.xpath('//li[@class="shop-infoo-list-item clearfix"]'):
            name = i.xpath(".//a[2]/h3/text()").extract_first().strip()
            score = i.xpath(".//p/a[1]/span[2]/text()").re_first('(\d+)分').strip()
            mean_price = i.xpath(".//p/a[2]/span[1]/text()").re_first('(\d+)').strip()

            yield RestaurantItem(
                name = name,
                score = float(score),
                mean_price = int(mean_price)
            )
