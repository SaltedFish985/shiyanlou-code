import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):

    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        
        url_list = ['https://github.com/shiyanlou?tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODowNTo1MyswODowMM4FkpPn&tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0zMFQxMzoxNDoxMiswODowMM4ByqPp&tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wMlQxNDo1MTowNiswODowMM4Bo0VK&tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0wOS0xNlQwOTo1NTo0MSswODowMM4Bb3PX&tab=repositories']
        return url_list

    def parse(self, response):
        for github in response.css('div#user-repositories-list li'):
            yield {
                'name': github.css('h3 a::text').extract_first().strip(),
                'update_time': github.css('relative-time ::attr(datetime)').extract_first().strip(),
            }