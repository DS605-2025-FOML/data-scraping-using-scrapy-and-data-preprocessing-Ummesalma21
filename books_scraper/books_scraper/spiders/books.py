import scrapy
from ..items import BooksScraperItem

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
    'https://books.toscrape.com/',
    ]

    def parse(self, response):
        all_books = response.css('article.product_pod')

        for book in all_books:
            items = BooksScraperItem()

            title = book.css('.product_pod h3 a::attr(title)').extract_first()
            price = book.css('.price_color::text').extract_first()
            stock_availability = book.css('.availability::text').extract()[-1].strip()
            thumbnail = book.css('.thumbnail::attr(src)').extract_first()
            rating = book.css('.star-rating::attr(class)').extract_first().split()[-1]

            items['title'] = title
            items['price'] = price
            items['stock_availability'] = stock_availability
            items['thumbnail'] = thumbnail
            items['rating'] = rating

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)