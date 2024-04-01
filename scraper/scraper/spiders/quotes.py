import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest
from elasticsearch import Elasticsearch
import datetime


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/js/page/"+str(i+1) for i in range(10)]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                endpoint='render.html',
                args={'wait': 0.5}
            )
    
    def parse(self, response):
        es = Elasticsearch("http://localhost:9200")
        for q in response.css("div.quote"):
            quote = dict()
            quote["author"] = q.css(".author::text").extract_first()
            quote["quote"] = q.css(".text::text").extract_first()
            quote["tags"] = q.css(".tags .tag::text").extract()
            quote["timestamp"] = datetime.datetime.now().isoformat()
            es.index(index="quotes", body=quote)

        page = response.url[response.url.index("page/")+5:]
        print("page=", page)