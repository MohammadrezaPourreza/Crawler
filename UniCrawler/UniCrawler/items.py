# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnicrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CourseItem(scrapy.Item):
    course_uni_url = scrapy.Field()
    course_title = scrapy.Field()
    course_url = scrapy.Field()
    course_prof = scrapy.Field()
    course_semester = scrapy.Field()
    course_department = scrapy.Field()
    course_lamguage = scrapy.Field()
    course_exam_from = scrapy.Field()
    course_credits = scrapy.Field()
    course_weeks = scrapy.Field()
    course_summary = scrapy.Field()
    course_remark = scrapy.Field()
    course_score = scrapy.Field()
    course_prerequest_for = scrapy.Field()
    course_teaching_method = scrapy.Field()
    course_outcome = scrapy.Field()
    course_skills = scrapy.Field()
class ProfessorItem(scrapy.Item):
    professor_name = scrapy.Field()
    professor_email = scrapy.Field()
    professor_landingPage = scrapy.Field()
    professor_phoneNumber = scrapy.Field()
    pass