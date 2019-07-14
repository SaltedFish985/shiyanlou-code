import scrapy

class PageItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
