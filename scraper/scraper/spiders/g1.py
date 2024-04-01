import scrapy
import base64


class NewsBr1Spider(scrapy.Spider):
    name = 'news_br_1'
    encoded_domains = 'ZzEuZ2xvYm8uY29t'
    encoded_urls = 'aHR0cHM6Ly9nMS5nbG9iby5jb20v'
    allowed_domains = [base64.b64decode(encoded_domains).decode()]
    start_urls = [base64.b64decode(encoded_urls).decode()]

    def parse(self, response):
        # Extract all news links from the home page
        news_links = response.css('a.feed-post-link::attr(href)').getall()
        for link in news_links:
            yield response.follow(link, self.parse_new)

    def parse_new(self, response):
        # Extract news details and build the item
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'content': response.css('h2.content-head__subtitle::text').get(),
            'publication_date': response.css('time[itemprop="datePublished"]::text').get().strip()
        }
