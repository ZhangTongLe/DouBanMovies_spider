from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import chardet
from ..items import DoubanmoviesItem

def process_chardet(string):
    try:
        coding = chardet.detect(string)['encoding']
        return string.decode(coding).encode('utf-8')
    except:
        return string.encode('utf-8')


class DouBanMovies_spider(CrawlSpider):
    name = 'DouBanMovies'
    start_urls = [
        'https://movie.douban.com/subject/26754513/?from=subject-page',
        'https://movie.douban.com/subject/26630167/?from=subject-page'
    ]
    allowed_domains = []
    rules = (
        Rule(LinkExtractor(allow=(r"https://movie\.douban\.com/subject/\d+/\?from=subject-page")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DoubanmoviesItem()
        name = ''.join(response.xpath('//span[@property="v:itemreviewed"]/text()').extract())
        stars = ''.join(response.xpath('//strong[@class="ll rating_num"]/text()').extract())
        try:
            name = process_chardet(name)
            stars = process_chardet(stars)
            stars = float(stars) if stars else 0
            item['movie_name'] = name
            item['movie_stars'] = stars
            yield item
        except Exception, e:
            print str(e)
