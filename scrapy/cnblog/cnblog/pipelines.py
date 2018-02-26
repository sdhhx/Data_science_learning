# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

from scrapy import signals
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

class JsonWithEncodingPipeline(object):
	def __init__(self):
		self.file = codecs.open('result.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

	def spider_closed(self, spider):
		self.file.close()

class MySQLStoreCnblogsPipeline(object):
	def __init__(self, dbpool):
		self.dbpool = dbpool
	
	@classmethod
	def from_settings(cls, settings):
		dbargs = dict(
			host=settings['MYSQL_HOST'],
			db=settings['MYSQL_DBNAME'],
			user=settings['MYSQL_USER'],
			passwd=settings['MYSQL_PASSWD'],
			charset='utf8',
			cursorclass = MySQLdb.cursors.DictCursor,
			use_unicode= True,
		)
		dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
		return cls(dbpool)

	#pipeline默认调用
	def process_item(self, item, spider):
		d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
		d.addErrback(self._handle_error, item, spider)
		d.addBoth(lambda _: item)
		return d
	#将每行更新或写入数据库中
	def _do_upinsert(self, conn, item, spider):

		query_command = "select 1 from `cnblogsinfo058` where url = '" + item['url'] + "'"
		conn.execute(query_command)
		ret = conn.fetchone()

		if ret:
			update_cpmmand = "update cnblogsinfo058 set title = '" + item['title'] + "'," + " summary = '" + item['summary'] + "'," +" id ='" + \
			item['id'] + "'," + " recommand = " + item['recommand'] + "," + " comment = " + item['comment'] + "," + " view = " + item['view'] + \
			" where url = '" + item['url'] + "'"
			print update_cpmmand
			conn.execute(update_cpmmand)
		else:
			insert_command = "insert into cnblogsinfo058(title, url, summary, id, recommand, comment, view) values('" + item['title'] + "','" + \
				item['url'] + "','" + item['summary'] + "','" + item['id'] + "'," + item['recommand'] + "," + item['comment'] + "," \
				+ item['view'] + ")"
			print insert_command
			conn.execute(insert_command)

	def _handle_error(self, failue, item, spider):
		log.err(failure)
