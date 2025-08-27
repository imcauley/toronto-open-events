import scrapy


class HarbourfrontSpider(scrapy.Spider):
    name = "harbourfront"
    start_urls = ["https://harbourfrontcentre.com/whats-on/"]

    def parse(self, response):
        event_htmls = self.get_all_events(response)
        with open(self.name + ".jsonl", "a") as file:
            for e in event_htmls:
                file.write(str(self.event_html_to_object(e)) + "\n")

    def get_all_events(self, response):
        return response.xpath(
            '//div[contains(@class, "wo-event")][not(contains(@class, "wo-event-copy"))]'
        )

    def event_html_to_object(self, event_html):
        return {
            "date": event_html.xpath("*/div[1]/div[1]/text()").get().strip(),
            "title": event_html.xpath("*/div[1]/div[2]/text()").get().strip(),
            "link": event_html.xpath("a/@href").get(),
            "description": event_html.xpath("*/div[1]/div[4]/text()").get().strip(),
        }
