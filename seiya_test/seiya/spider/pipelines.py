from ..db import Job, House, Restaurant, session
from .items import JobItem, HouseItem, RestaurantItem

class SeiyaPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, JobItem):
            return self._process_jobitem(item)
        elif isinstance(item, HouseItem):
            return self._process_houseitem(item)
        elif isinstance(item, RestaurantItem):
            return self._process_restaurantitem(item)

    def _process_jobitem(self, item):
        session.add(Job(**item))

    def _process_houseitem(self, item):
        session.add(House(**item))

    def _process_restaurantitem(self, item):
        session.add(Restaurant(**item))

    def close_spider(self, spider):
        session.commit()
        session.close()