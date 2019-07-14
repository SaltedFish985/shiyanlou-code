import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
    	item['text'] = re.sub(r'\s+', ' ', item['text'])
    	data = json.dumps(dict(item))
    	redis.lpush('flask_doc:items', data)
        return item

    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
