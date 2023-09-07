import scrapy
import re
from scrapy.exceptions import CloseSpider
from phonesScraper.items import PhonesItems

class phonesScraper(scrapy.Spider):
    name = "phones"

    # Setting the starting page number for scraping
    def __init__(self):
        self.page_number = 1

    # Sending requests to website
    def start_requests(self):
        start_url = "https://www.productindetail.com/phones/page-1"
        yield scrapy.Request(start_url, callback=self.parse)

    # Checking the request status and visiting each phone link.
    def parse(self, response):
        if response.status == 200:
            self.logger.info("Request was successful")
        else:
            raise CloseSpider("Recieved 404 response")

        phone_divs = response.css('div.col-md-6.col-lg-4.col-xl-3.col-xxl-2.mb-4')
        for phone_div in phone_divs:
            phone_link = phone_div.css('a::attr(href)').get()
            yield response.follow(phone_link, callback=self.parse_phone)

        self.page_number += 1
        next_page = f'https://www.productindetail.com/phones/page-{self.page_number}/'
        yield response.follow(next_page, callback=self.parse)

    # Scrapping data and saving it to class
    def parse_phone(self, response):
        
        phone_item = PhonesItems()
        display_text = response.xpath('//div[@class="card rounded-0 mb-2" and @id="display"]//td[@class="border-end"]//small/text()').get()
        os = response.xpath('//div[@class="col-sm-6 col-lg-4 mb-4"][4]//small/text()').get()  

        phone_item["product_name"] = response.xpath('//strong/text()').get()
        phone_item["brand"] = response.xpath('(//a[@class="link-dark text-decoration-none"]/small/text())[2]').get()
        phone_item["link"] = response.xpath('//img[@class="img-fluid mb-3"]/@src').get()
        
        if display_text:
            if re.search(r'\d', display_text):
                phone_item["display_technology"] = "Not provided"
            else:
                phone_item["display_technology"] = display_text
    
        if os == "Operating System ":
            phone_item["os"] = response.xpath('(//div[@class="col-sm-6 col-lg-4 mb-4"][4]//small/text())[2]').get()
        else:
            phone_item["os"] = "Not provided"  

        yield phone_item