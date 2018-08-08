import scrapy


class MicrosoftItem(scrapy.Item):
    App_Name = scrapy.Field()
    Url = scrapy.Field()
    Rating = scrapy.Field()
    Num_Rated = scrapy.Field()
    Category = scrapy.Field()
    Comment_header = scrapy.Field()
    Comment_rating = scrapy.Field()
    Num_Reviewed = scrapy.Field()
    ESRB_rating = scrapy.Field()


