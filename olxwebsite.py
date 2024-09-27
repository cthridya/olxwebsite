import scrapy

class OlxwebsiteSpider(scrapy.Spider):
    name = "olxwebsite"
    start_urls = ["https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"]

    def parse(self, response):
        property_links = response.xpath('//li[contains(@class, "_1DNjI")]/a/@href').getall()

        for link in property_links:
            yield response.follow(link, self.parse_property)

        next_page = response.xpath('//a[@data-aut-id="btnLoadMore"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_property(self, response):
        yield {


            'price': response.xpath('//span[@data-aut-id="itemPrice"]/text()').get().replace('₹', '').strip(),
            'image_url': response.xpath('//img/@src').get(),
            'breadcrumbs': response.xpath('//div[@data-aut-id="breadcrumb"]//li/a/text()').getall(),
            'seller_name': response.xpath('//div[@class="_2tgkn"]/a/div[@class="eHFQs"]/text()').get(),
            

            }

      
