import scrapy
import coloredlogs



class NaverSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        urls = ["https://hdhd253.net"]
        for url in urls:
            yield scrapy.Request(
                url=url, callback=self.parse, errback=self.errback
            )

    def parse(self, response):
        self.logger.info("***************")
        self.logger.info(response.request)
        self.logger.info(response.status)
        self.logger.info(repr(response))
        self.logger.info(response.request.meta.get("redirect_url"))
        self.logger.info(response.request.url)
        self.logger.info(response.request.meta.get("redirect_urls", []) + [
                response.request.url
            ])
        self.logger.info("***************")
        yield{
            'title':response.xpath("//title").get(),
            'response_status': response.status,
            'redirect':response.request.meta.get("redirect_urls", []) + [
                response.request.url
            ]
        }

    def errback(self, failure):
        self.logger.warning("****************************")
        self.logger.warning(failure)
        self.logger.warning(repr(failure))
        self.logger.warning("****************************") 