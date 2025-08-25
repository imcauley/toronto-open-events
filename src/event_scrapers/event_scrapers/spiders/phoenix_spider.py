import scrapy


class PhoenixSpider(scrapy.Spider):
    name = "phoenix"
    start_urls = ["https://thephoenixconcerttheatre.com/events/page/1"]

    def parse(self, response):
        event_htmls = self.get_all_events(response)
        with open(self.name + ".jsonl", "a") as file:
            for e in event_htmls:
                file.write(str(self.event_html_to_object(e)) + "\n")

    def get_all_events(self, response):
        return response.css(".event-item")

    def event_html_to_object(self, event_html):
        return {
            "date": event_html.css("header.event-date::text").get().strip(),
            "title": event_html.css("span.sr-only::text").get(),
            "link": event_html.css("a").attrib["href"],
        }
