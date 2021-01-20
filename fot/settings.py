BOT_NAME = 'fot'

SPIDER_MODULES = ['fot.spiders']
NEWSPIDER_MODULE = 'fot.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'fot.pipelines.FotPipeline': 100,

}