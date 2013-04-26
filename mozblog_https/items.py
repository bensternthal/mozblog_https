# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class MozblogHttpsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    iframe = Field()
    image = Field() 
    script = Field()
    url = Field()
