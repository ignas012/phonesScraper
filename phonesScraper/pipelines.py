import pymongo
from scrapy.exceptions import DropItem

class MongoDBPipeline(object):

    # Initializing MongoDBPipeline with crawler settings and establishing a connection to MongoDB.
    def __init__(self, crawler):
        self.crawler = crawler
        self.connection = pymongo.MongoClient(
            crawler.settings.get('MONGODB_SERVER'),
            crawler.settings.get('MONGODB_PORT')
        )
        db = self.connection[crawler.settings.get('MONGODB_DB')]
        self.collection = db[crawler.settings.get('MONGODB_COLLECTION')]

    # Creating an instance of MongoDBPipeline using the provided crawler.
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        return cls(crawler)

# Processing the received phone_item, checking for missing data, and inserting it into the MongoDB collection if valid.
    def process_item(self, phone_item, spider):
        valid = True
        for data in phone_item:
            if not phone_item[data]:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert_one(dict(phone_item))
        return phone_item