import datetime
import scrapy
from scrapy.loader import ItemLoader
from urllib.parse import urlencode

# from event_scrapers.event_item import EventItem
# from event_scrapers.event_listing import EventListing


# class CrowsTheatreSpider(scrapy.Spider):
#     name = "crows_theatre"
#     start_urls = ["https://www.crowstheatre.com/shows-events/schedule?p=10"]

#     shared_attributes = {
#         "organizer": "Crows Theatre",
#     }

#     def parse(self, response):
#         available_months = response.xpath('//select[@id="select-month"]/option')
#         for available_month in available_months:
#             val = available_month.attrib["value"]
#             next_url = self.start_urls[0] + urlencode({"month": val})
#             yield response.follow(next_url, self.parse_event_page)

#     def parse_event_page(self, response):
#         event_htmls = self.get_all_events(response)
#         for event in event_htmls:
#             self.event_html_to_object(event)

#     def get_all_events(self, response):
#         return response.xpath('//div[@class="schedule"]/div')

#     def event_html_to_object(self, event_html):
#         loader = ItemLoader(item=EventListing, response=event_html)
#         loader.add_value("name", "test")
#         loader.add_value("organizer", "test")
#         loader.add_value("start_date", datetime.datetime.now())
#         return loader.load_item()
#         # return {
#         #     "date": event_html.xpath("*/div[1]/div[1]/text()").get().strip(),
#         #     "name": event_html.xpath("*/div[1]/div[2]/text()").get().strip(),
#         #     "link": event_html.xpath("a/@href").get(),
#         #     "description": event_html.xpath("*/div[1]/div[4]/text()").get().strip(),
#         #     **self.shared_attributes,
#         # }
