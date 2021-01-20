import scrapy

from scrapy.loader import ItemLoader
import re

from ..items import FotItem


class FotSpider(scrapy.Spider):
	name = 'fot'
	start_urls = ['https://www.fot.bg/blog']

	def parse(self, response):
		post_links = response.xpath('//div[@class="simpleblog__listing__post__wrapper__content"]/h3/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		pagination_links = response.xpath('//nav[@class="simpleblog__listing__pagination pagination"]/div/ul/li/a[@rel="next"]/@href')
		yield from response.follow_all(pagination_links, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="simpleblog__post__content"]/descendant-or-self::*/text()').getall()
		description = [re.sub(' ', '', p).strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//time/text()').get().strip()[:-3]

		item = ItemLoader(item=FotItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
