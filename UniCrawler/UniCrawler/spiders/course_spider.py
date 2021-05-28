import scrapy
import csv
from scrapy.selector import Selector
from ..items import ProfessorItem

class ProfSpider(scrapy.Spider):
    header = ['university_url', 'course_title', 'course_url', 'course_prof', 'course_semester', 'course_department',
              'course_language', 'course_exam_from', 'course_credits', 'course_weeks', 'course_summary',
              'course_remark', 'course_score', 'course_prerequest_for', 'course_teaching_method', 'course_outcome',
              'course_skills']
    with open('courses.csv', 'a+',encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        f.close()
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
        # header = ['university_url','course_title', 'course_url', 'course_prof', 'course_semester', 'course_department','course_language','course_exam_from','course_credits','course_weeks','course_summary','course_remark','course_score','course_prerequest_for','course_teaching_method','course_outcome','course_skills']
        url = response.request.url
        course_title = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_XMATIERE_EN"]/text()').get()
        course_prof = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_ENSEIGNANTS"]/text()').get()
        course_semester = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_PERIODE_SEMESTRE"]/text()').get()
        course_department = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_SECTIONS"]/text()').get()
        course_language = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_MATIERE_LANGUE"]/text()').get()
        course_exam_from = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_FORME_EXA"]/text()').get()
        course_credits = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_ECTS_OU_COEFF"]/text()').get()
        course_weeks = Selector(response=response).xpath('//fiche/texte[@var="ITEMPLAN_SEMAINES"]/text()').get()
        course_summary = Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_RESUME"]/text()').get()
        course_remark = Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_REMARQUE_PLAN"]/text()').get()
        course_score = Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_METHODE_EVALUATION"]//p/text()').get()
        course_prerequest_for = Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_PREPARATION_POUR"]//p/text()').get()
        course_teaching_method= Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_METHODE_ENSEIGNEMENT"]//p/text()').get()
        course_outcome = Selector(response=response).xpath('//fiche/texte[@var="RUBRIQUE_ACQUIS_FORMATION"]//li/text()').getall()
        course_skills = Selector(response=response).xpath('//fiche/texte[@var="COMPETENCES_TRANS_ITEMPLAN"]//li/text()').getall()
        course_outcome = ' '.join(course_outcome)
        course_skills = ' '.join(course_skills)
        course_department = course_department[0:course_department.index('(')]
        with open('courses.csv', 'a+',encoding='utf8', newline='') as f:
            writer = csv.writer(f,lineterminator="\n")
            temp = []
            temp.append('https://www.epfl.ch/en/')
            temp.append(str(course_title))
            temp.append(str(url))
            temp.append(str(course_prof))
            temp.append(str(course_semester))
            temp.append(str(course_department))
            temp.append(str(course_language))
            temp.append(str(course_exam_from))
            temp.append(str(course_credits))
            temp.append(str(course_weeks))
            temp.append(str(course_summary))
            temp.append(str(course_remark))
            temp.append(str(course_score))
            temp.append(str(course_prerequest_for))
            temp.append(str(course_teaching_method))
            temp.append(str(course_outcome))
            temp.append(str(course_skills))
            writer.writerow(temp)
            f.close()
