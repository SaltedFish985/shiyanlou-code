import scrapy

class FlaskItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()