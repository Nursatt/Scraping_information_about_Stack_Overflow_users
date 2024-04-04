import scrapy

class UserItem(scrapy.Item):
    username = scrapy.Field()
    location = scrapy.Field()
    reputation = scrapy.Field()
    tags = scrapy.Field()
