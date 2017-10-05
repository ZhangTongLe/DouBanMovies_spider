# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sql import DataBase

database = DataBase()
class DoubanmoviesPipeline(object):
    def process_item(self, item, spider):
        database.insert_into_db(item['movie_name'], item['movie_stars'])
        print u'插入数据库成功!!'
        return item
