from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#scrapy规则爬虫
class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'atguigu'
    allowed_domains = ['atguigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    rules = [

        # Rule(LinkExtractor(restrict_css=('.top-cat', '.sub-cat', '.cat-item')
        # ), callback='parse_directory', follow=True),
        Rule(LinkExtractor(allow=r"download"), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }


        yield {
            'name': response.xpath('//title/text()').extract_first(),
            'description': response.xpath('//meta[@name="keywords"]/@content').extract_first().strip(),
            'link': response.url,
        }

        # for div in response.xpath('//div[@class="item"]'):
		  #
		  #
        #     yield {
        #         'name': div.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first(),
        #         'description': div.xpath('.//div[@class="bd"]/p/text()').extract_first().strip(),
        #         'link': div.url,
        #     }
