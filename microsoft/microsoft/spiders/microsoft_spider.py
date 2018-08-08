from scrapy import Spider, Request
from microsoft.items import MicrosoftItem
import re

class MicrosoftSpider(Spider):
    name = "microsoft_spider"
    allowed_urls = ['https://www.microsoft.com/en-us/store/top-free/apps/pc/']
    start_urls = ['https://www.microsoft.com/en-us/store/top-free/apps/pc?s=store&skipitems='+ str(i*90) for i in range(13)]

    def parse(self, response):
        values = response.xpath('//*[@id="productPlacementList"]/div[3]/div/section')
        for value in values:
            Url=value.xpath('.//a/@href').extract_first()
            result_urls='https://www.microsoft.com' + str(Url)
            yield Request(url=result_urls, callback=self.parse_app_page)

    def parse_app_page(self, response):
        comment_values=response.xpath('//div[@class="srv_reviews"]/div')
        for value in comment_values:

            App_Name=value.xpath('//h1/text()').extract_first()

            link_category=value.xpath('//div/span/span/a/@href').extract_first()
            Category=re.split('&', (re.split('=', link_category)[1]))[0]

            Rating=value.xpath('//div/a/meta/@content')[0].extract()
            Num_Rated=value.xpath('//div/a/meta/@content')[1].extract()

            Comment_header=value.xpath('.//h5/@aria-label').extract()
            Comment_rating=value.xpath('.//p/span[1]').extract_first()[29]

            ESRB_rating=value.xpath('//a/@aria-label')[4].extract()
            Num_Reviewed=value.xpath('//div[@class="context-pagination"]/span/text()').extract_first()
            #Num_Reviewed=''.join(re.findall(r'\d+', Num_Reviewed[8:len(Num_Reviewed)]))


            item = MicrosoftItem()
            item['App_Name'] = App_Name
            item['Rating'] = Rating
            item['Num_Rated'] = Num_Rated
            item['Category'] = Category
            item['Comment_header'] = Comment_header
            item['Comment_rating'] = Comment_rating
            item['Num_Reviewed'] = Num_Reviewed
            item['ESRB_rating'] = ESRB_rating
            yield item
