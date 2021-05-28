import scrapy
import csv
from scrapy.selector import Selector
from ..items import CourseItem
from ..items import ProfessorItem

class ProfSpider(scrapy.Spider):
    name = 'courses'
    # allowed_domains = ["epfl.ch"]
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
        items = CourseItem()
        items['course_uni_url'] = 'https://www.epfl.ch/en/'
        items['course_url'] = response.request.url
        items['course_title'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_XMATIERE_EN"]/text()').get()).strip()
        items['course_prof'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_ENSEIGNANTS"]/text()').get()).strip()
        items['course_semester'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_PERIODE_SEMESTRE"]/text()').get()).strip()
        course_department = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_SECTIONS"]/text()').get()).strip()
        items['course_lamguage'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_MATIERE_LANGUE"]/text()').get()).strip()
        items['course_exam_from'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_FORME_EXA"]/text()').get()).strip()
        items['course_credits'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_ECTS_OU_COEFF"]/text()').get()).strip()
        items['course_weeks'] = str(Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_SEMAINES"]/text()').get()).strip()
        items['course_summary'] = str(Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_RESUME"]/text()').get()).strip()
        items['course_remark'] = str(Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_REMARQUE_PLAN"]/text()').get()).strip()
        items['course_score'] = str(Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_METHODE_EVALUATION"]//p/text()').get()).strip()
        items['course_prerequest_for'] = str(Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_PREPARATION_POUR"]//p/text()').get()).strip()
        items['course_teaching_method']= str(Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_METHODE_ENSEIGNEMENT"]//p/text()').get()).strip()
        course_outcome = Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_ACQUIS_FORMATION"]//li/text()').getall()
        course_skills = Selector(response=response).xpath('//fiche/texte[@var="COMPETENCES_TRANS_ITEMPLAN"]//li/text()').getall()
        items['course_outcome'] = ' '.join(course_outcome)
        items['course_skills'] = ' '.join(course_skills)
        items['course_department'] = course_department[0:course_department.index('(')]
        yield items