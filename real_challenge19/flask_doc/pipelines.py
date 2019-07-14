import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        item['text'] = re.sub(r'\s+', ' ', item['text'])
        self.redis.lpush('flask_doc:items', json.dumps(dict(item)))
        return item

    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
