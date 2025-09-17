from scrapy.item import Item, Field


class EventItem(Item):
    name = Field()
    organizer = Field()
    start_date = Field()
    end_date = Field()
    url = Field()
    location = Field()
    description = Field()
    tags = Field()
    additional_attributes = Field()
