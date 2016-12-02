# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
    # See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch

class SearchEnginePipeline(object):
    def __init__(self):
        self.elasticsearch = Elasticsearch('localhost:9200')

    def process_item(self, item, spider):
        self.elasticsearch.index(index='spider_test', doc_type='test', body=item)
        return item
