# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class MoviePipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('movie.db')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('''CREATE TABLE Movie
               (ID            INTEGER PRIMARY KEY autoincrement,
               NAME           VARCHAR(1024)     NOT NULL,
               movieInfo      VARCHAR(1024)     NOT NULL,
               star           VARCHAR(16)       DEFAULT NULL,
               quote          VARCHAR(1024)     DEFAULT NULL,
               createtime     DATETIME          DEFAULT CURRENT_TIMESTAMP);''')
            self.conn.commit()    
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        self.cursor.execute("INSERT into Movie (name,movieInfo,star,quote) VALUES (?,?,?,?)", (
            item['title'], item['movieInfo'], item['star'], item['quote']))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()