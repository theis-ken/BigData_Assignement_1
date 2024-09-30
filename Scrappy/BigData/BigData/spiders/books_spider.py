import scrapy
from scrapy.exceptions import CloseSpider

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        if response.status != 200:
            self.logger.error(f"Failed to retrieve {response.url} - Status code: {response.status}")
            return

        for book in response.css('article.product_pod'):
            try:
                title = book.css('h3 a::attr(title)').get()
                price = book.css('div.product_price p.price_color::text').get()
                availability = book.css('p.instock.availability::text').re_first('\S+')

                if not title or not price:  # Check for missing fields
                    raise ValueError("Missing title or price")

                price = float(price.replace('£', '').strip())
                availability = availability.strip() if availability else 'Unknown'

                yield {
                    'title': title,
                    'price': price,
                    'availability': availability,
                }
            except Exception as e:
                self.logger.error(f"Error processing book: {e}")

        # Pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            self.logger.info(f"Following pagination link: {next_page}")  # Logging the pagination link
            yield response.follow(next_page, self.parse, errback=self.handle_error)



    def handle_error(self, failure):
        self.logger.error(repr(failure))
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error(f"HttpError on {response.url}")
        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error(f"DNSLookupError on {request.url}")
        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error(f"TimeoutError on {request.url}")
