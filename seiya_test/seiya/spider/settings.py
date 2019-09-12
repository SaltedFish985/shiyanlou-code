# -*- coding: utf-8 -*-

# Scrapy settings for seiya project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'seiya'

SPIDER_MODULES = ['seiya.spider.spiders']
NEWSPIDER_MODULE = 'seiya.spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'seiya (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
#    'Connection': 'keep-alive',
#    'Cookie': 'privacyPolicyPopup=false; user_trace_token=20190515145327-a25533be-aa04-4695-895c-38b1971d8e24; _ga=GA1.2.972005731.1557903211; LGUID=20190515145333-27bf06a2-76de-11e9-95f3-525400f775ce; _gid=GA1.2.299339334.1566214364; LG_HAS_LOGIN=1; hasDeliver=0; gate_login_token=839650030e87ae62992fb24f16361955888990aac080083958ca45634b584ef0; JSESSIONID=ABAAABAAAFCAAEG0A47F0442E50F6331DFB7D1AE58F661B; WEBTJ-ID=20190820153748-16cadf5e341416-0a2ce7ea524b1a-48774f16-1049088-16cadf5e3462d0; _putrc=BE08C183E8C0189D123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B70944; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; privacyPolicyPopup=false; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566118688,1566214364,1566286669; _gat=1; LGSID=20190820153749-68c7adb5-c31d-11e9-a503-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; SEARCH_ID=84383a7315a44ccc845af0c99f9e0c46; X_HTTP_TOKEN=9e31de4b62150c0b0076826651dd4efc9acc2cde96; LGRID=20190820153820-7ba4b9ab-c31d-11e9-a503-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566286701',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'seiya.spider.middlewares.SeiyaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'seiya.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'seiya.spider.pipelines.SeiyaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
