import scrapy

class JobItem(scrapy.Item):
    title = scrapy.Field()
    city = scrapy.Field()
    salary_low = scrapy.Field()
    salary_up = scrapy.Field()
    experience_low = scrapy.Field()
    experience_up = scrapy.Field()
    education = scrapy.Field()
    tags = scrapy.Field()
    company = scrapy.Field()

class HouseItem(scrapy.Item):
    housing_estate = scrapy.Field()
    area = scrapy.Field()
    orientations = scrapy.Field()
    apartment = scrapy.Field()
    rent = scrapy.Field()

class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    mean_price = scrapy.Field()
