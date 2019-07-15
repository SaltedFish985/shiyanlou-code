from scrapy.exceptions import DropItem
import json
import re
import redis

class DoubanMoviePipeline(object):
    
    def process_item(self, item, spider):
        item['score'] = float(item['score'])
        if item['score'] < 8.0:
            raise DropItem()
        else:
            item['summary'] = re.sub(r'\s+', ' ', item['summary'])
            self.redis.lpush('douban_movie:items', json.dumps(dict(item)))
            return item
    
    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)