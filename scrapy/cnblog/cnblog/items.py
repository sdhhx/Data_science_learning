# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	url = scrapy.Field()
	summary = scrapy.Field()
	id = scrapy.Field()
	recommand = scrapy.Field()
	comment = scrapy.Field()
	view = scrapy.Field()
	pass
