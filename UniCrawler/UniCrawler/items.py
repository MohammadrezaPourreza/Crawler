# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnicrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ProfessorItem(scrapy.Item):
    professor_name = scrapy.Field()
    professor_email = scrapy.Field()
    professor_landingPage = scrapy.Field()
    professor_phoneNumber = scrapy.Field()
    pass