#!/usr/bin/python3

import requests
import SpiderUtil
import os
from lxml import etree
from LessonVideoSpider import VideoSpider


class CoursePathSpider(object):

    """ 课程路径图网页分析 """

    # 课程章路径
    XPATH_CHAPTER = '//*[@id="container"]/div/div[@class="pathstage mar-t30"]'
    # 章节名
    xpath_chapter_name = 'div[@class="pathstage-txt"]/h2/text()'
    # 章下的课程列表路径
    xpath_chapter_lesson_list = 'div/div[@class="stagewidth lesson-list"]/ul[@class="cf"]/li'
    # 课程名和链接
    xpath_lesson_name = 'div[@class="lesson-infor"]/h2[@class="lesson-info-h2"]/a/text()'
    xpath_lesson_link = 'div[@class="lesson-infor"]/h2[@class="lesson-info-h2"]/a/@href'

    def __init__(self, url, simple_name):
        super(CoursePathSpider, self).__init__()
        self.url = url
        self.simple_name = simple_name
        self.response = None
        self.chapter_list = []
        self.selector = None
        self.title = ''
        self.chapter_list = []

    def parse_html(self):
        print("正在打开网址：", self.url)
        self.response = requests.get(self.url)
        print("开始处理返回结果...")
        self.selector = etree.HTML(self.response.text)
        self.title = self.selector.xpath('//title/text()')[0]
        if self.simple_name == '':
            if len(self.title) > 10:
                self.simple_name = self.title[0, 10]
            else:
                self.simple_name = self.title

        print("课程名称：", self.title)
        for chapterEle in self.selector.xpath(CoursePathSpider.XPATH_CHAPTER):
            self.add_chapter(_Chapter(chapterEle))

    def add_chapter(self, chapter):
        if isinstance(chapter, _Chapter):
            self.chapter_list.append(chapter)
        else:
            raise ValueError("chapter is not a instance of Chapter")

    def download(self, path, index='a'):
        path = path + "/" + self.simple_name
        if SpiderUtil.is_all(index):
            print("下载完整路线")
            self.download_all(path)
        else:
            index2 = SpiderUtil.is_valid_index(index, len(self.chapter_list))
            print("下载：" + self.chapter_list[index2].name)
            return self.chapter_list[index2].download(path)

    def download_all(self, path):
        for chapter in self.chapter_list:
            chapter.download(path)
        print("课程路线：", self.title, '保存成功')

    def show(self):
        print(self.title)
        for chapter in self.chapter_list:
            chapter.show()

    def lessons(self):
        lesson_list_2 = []
        for chapter in self.chapter_list:
            lesson_list_2.extend(chapter.lessonlist)
        return lesson_list_2


class _Chapter(object):

    """按章分析 """

    def __init__(self, selector):
        super(_Chapter, self).__init__()
        self.selector = selector
        self.lesson_list = []
        self.name = ""
        self.parse_html()

    def parse_html(self):
        self.name = self.selector.xpath(CoursePathSpider.xpath_chapter_name)[0]
        print(self.name)
        index = 0
        for lessonEle in self.selector.xpath(CoursePathSpider.xpath_chapter_lesson_list):
            index += 1
            self.add_lesson(_Lesson(lessonEle, pre_name=str(index) + ". "))

    def add_lesson(self, lesson):
        if isinstance(lesson, _Lesson):
            self.lesson_list.append(lesson)
        else:
            raise ValueError("lesson is not a instance of Lesson")

    def download(self, path, index='a'):
        if SpiderUtil.is_all(index):
            self.download_all(path)
        else:
            index2 = SpiderUtil.is_valid_index(index, len(self.lesson_list))
            if index2 != 0:
                print("下载：" + self.lesson_list[index2].name)
                return self.lesson_list[index2].download(path)
            else:
                return "error"
        return "OK"

    def download_all(self, parent):
        path = parent + "/" + self.name
        for lesson in self.lesson_list:
            lesson.download(path)
            # result =
            # if not SpiderUtil.is_ok(result):
            #     break

    def show(self):
        print(self.name)
        for lesson in self.lesson_list:
            lesson.show()


class _Lesson(object):
    """分析课程信息 """
    def __init__(self, selector, pre_name=''):
        self.selector = selector
        self.name = pre_name + selector.xpath(CoursePathSpider.xpath_lesson_name)[0]
        self.link = selector.xpath(CoursePathSpider.xpath_lesson_link)[0]
        self.path = ""
        self.sub_spider = VideoSpider()
        # print("--", self.name)

    def download(self, parent):
        self.path = parent + "/" + self.name
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            self.save_inf()
        print("正在下载课程：", self.name)
        self.sub_spider.download(self.path, self.link)
        self.sub_spider.save_info(self.path)

    def save_inf(self):
        file = open(self.path + "/readme.txt", "a+")
        file.write("#课程名称")
        file.write("\nname=" + self.name)
        file.write("\n#课程链接")
        file.write("\nlink=" + self.link)
        file.close()

    def show(self):
        print("-- ", self.name, "=", self.link)