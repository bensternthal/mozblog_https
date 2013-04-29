# Scrapy settings for mozblog_https project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mozblog_https'

SPIDER_MODULES = ['mozblog_https.spiders']
NEWSPIDER_MODULE = 'mozblog_https.spiders'

#DEPTH_LIMIT = 0
#DOWNLOAD_DELAY = 0.25 

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'scrapy_mozblog_https (+http://www.mozilla.org bsternthal@mozilla.com)'
