import scrapy

class ChallengeItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()