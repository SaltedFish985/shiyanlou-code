from sqlalchemy.orm import sessionmaker
from challenge.models import Repository, engine
from datetime import datetime
from datetime import timedelta

class ChallengePipeline(object):

    def process_item(self, item, spider):        
        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ') + timedelta(hours=8.0)    
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):        
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):        
        self.session.commit()
        self.session.close()
