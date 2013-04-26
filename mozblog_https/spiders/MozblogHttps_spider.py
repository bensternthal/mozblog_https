from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector 
from mozblog_https.items import MozblogHttpsItem

class MozblogHttpsSpider(CrawlSpider):
    name = "mozblog"
    allowed_domains = ["127.0.0.1"]
    start_urls = [
        "http://127.0.0.1:8080"
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_start_url')
    ]  

    # scrapy is weird
    # def parse_start_url(self, response):
    #     list(self.parse_item(response))

    def parse_start_url(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        item = MozblogHttpsItem()

        # Find http Image
        item['image'] = hxs.select('//img[contains(@src, "http://")]/@src').extract()

        # Find http Iframe
        item['iframe'] = hxs.select('//iframe[contains(@src, "http://")]/@src').extract()

        # Found anything bad, if so add to list
        if item['image'] or item['iframe']:
            item['url'] = response.url 
            items.append(item)

        return items

# Find images
# Find iframe
# Find embed?
# Find scripts