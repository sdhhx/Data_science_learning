# -*- coding: utf-8 -*-

import scrapy
from cnblog.items import CnblogItem

class cnblogSpider(scrapy.Spider):
	name = 'cnblogSpider'
	start_urls = ['https://www.cnblogs.com/pick']

	def parse(self, response):
		yield scrapy.Request(response.url, callback=self.parse_blog)
		for i in range(2,21):
			url = "https://www.cnblogs.com/pick/" + str(i) + "/"
			print "current_url: " + url
			yield scrapy.Request(url, callback=self.parse_blog)

	def parse_blog(self, response):
		for blog in response.xpath('//div[@class="post_item"]'):
			item = CnblogItem()
			item['title'] = blog.xpath('.//a[@class = "titlelnk"]/text()').extract_first().strip()
			item['url'] = blog.xpath('.//a[@class = "titlelnk"]/@href').extract_first()
			#取后一项，不包含图片元素
			item['summary'] = blog.xpath('.//p[@class = "post_item_summary"]/text()').extract()[-1].strip()
			item['id'] = blog.xpath('.//div[@class = "post_item_foot"]/a/text()').extract_first()
			item['recommand'] = blog.xpath('.//span/text()').extract_first()
			item['comment'] = blog.xpath('.//div[@class = "post_item_foot"]/span[1]/a/text()').extract_first().strip().split('(')[1].split(')')[0]
			item['view'] = blog.xpath('.//div[@class = "post_item_foot"]/span[2]/a/text()').extract_first().strip().split('(')[1].split(')')[0]
			#print item['title']
			#print item['url']
			#print item['summary']
			#print item['recommand']
			#print item['comment']
			#print item['view']
			#print "insert into cnblogsinfo(title, url, summary, id, recommand, comment, view) values(" + item['title'] + "," + \
			#item['url'] + "," + item['summary'] + "," + item['id'] + "," + item['recommand'] + "," + item['comment'] + "," \
			#+ item['view'] + ")"

			yield item