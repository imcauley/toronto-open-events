import datetime
import scrapy
from scrapy.loader import ItemLoader
from event_item import EventItem


class PhoenixSpider(scrapy.Spider):
    name = "phoenix"
    start_urls = ["https://thephoenixconcerttheatre.com/events/page/1"]

    def parse(self, response):
        event_htmls = self.get_all_events(response)
        for e in event_htmls:
            yield self.event_html_to_object(e)

    def get_all_events(self, response):
        return response.css(".event-item")

    def event_html_to_object(self, event_html):
        loader = ItemLoader(item=EventItem(), response=event_html)
        loader.add_value(
            "start_date", event_html.css("header.event-date::text").get().strip()
        )
        loader.add_value("name", event_html.css("span.sr-only::text").get())
        loader.add_value("organizer", "Phoenix Theatre")
        loader.add_value("start_date", datetime.datetime.now())
        loader.add_value("url", event_html.css("a").attrib["href"])
        return loader.load_item()
