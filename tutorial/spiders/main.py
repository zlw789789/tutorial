# -*- coding: utf-8 -*-

from scrapy import cmdline  
cmdline.execute("scrapy crawl douban_movie_250 -o info.csv -t csv".split())  