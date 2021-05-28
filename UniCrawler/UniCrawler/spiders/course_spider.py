import scrapy
import csv
from scrapy.selector import Selector
from ..items import ProfessorItem

class ProfSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ["epfl.ch"]
    start_urls = [
        "https://www.epfl.ch/education/international/en/coming-to-epfl/semester-courses/studies/english-master-courses/",
    ]
    def parse(self, response):
        for href in response.css('#content li ::attr(href)').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_general)

    def parse_general(self,response):
        for href in response.css('.includeBox a ::attr(href)').getall():
            enghref = href[0:-2]+'en'
            url = response.urljoin(enghref)
            yield scrapy.Request(url, callback=self.parse_each_course)

    def parse_each_course(self,response):
        course_title = Selector(response=response).xpath('//fiche/').get()
        # course_title = response.css('h2.noSpacing').get()
        print(course_title)
