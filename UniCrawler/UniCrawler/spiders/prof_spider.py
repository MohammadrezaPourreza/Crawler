import scrapy
import csv
from ..items import ProfessorItem

class ProfSpider(scrapy.Spider):
    name = 'professors'
    def start_requests(self):
        urls = [
            'https://www.epfl.ch/research/faculty-members/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ProfessorItem()
        professor_names = response.css('.contact-list-avatar+ .contact-list-item::text').getall()
        professor_LandingPage = response.css('.contact-list-avatar+ .contact-list-item ::attr(href)').getall()
        professor_postion = response.css('.m-0::text').getall()
        professor_phone_number = response.css('.text-muted:nth-child(5) ::attr(href)').getall()
        header = ['University','Abbreviation','Professor_name','Prodessor_landingPage','professor_postion','professor_phone_number']
        with open('professors.csv', 'w', encoding='latin1', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for i in range(1,len(professor_names)):
                temp = []
                temp.append('École polytechnique fédérale de Lausanne')
                temp.append('EPFL')
                temp.append(professor_names[i])
                temp.append(professor_LandingPage[i])
                temp.append(professor_postion[i])
                temp.append(professor_phone_number[i])
                writer.writerow(temp)
            f.close()