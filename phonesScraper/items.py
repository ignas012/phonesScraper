from scrapy.item import Item, Field

class PhonesItems(Item):
    product_name = Field()
    brand = Field()
    display_technology = Field()
    os = Field()
    link = Field()