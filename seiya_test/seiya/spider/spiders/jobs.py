import re
import scrapy
from ..items import JobItem


class JobSpider(scrapy.Spider):
    name = 'jobs'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'privacyPolicyPopup=false; user_trace_token=20190515145327-a25533be-aa04-4695-895c-38b1971d8e24; _ga=GA1.2.972005731.1557903211; LGUID=20190515145333-27bf06a2-76de-11e9-95f3-525400f775ce; LG_HAS_LOGIN=1; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; privacyPolicyPopup=false; JSESSIONID=ABAAABAAAFCAAEG15EAB5B8E5A0D23D46A417737C883136; WEBTJ-ID=20190821195647-16cb40958e5e9-097c55da252a9c-48774f16-1049088-16cb40958e612f; _gid=GA1.2.1032311511.1566388607; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566214364,1566286669,1566287407,1566388608; _gat=1; LGSID=20190821221300-c80681e5-c41d-11e9-a503-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; TG-TRACK-CODE=index_user; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cb48903da31e-047f11eacc848c-48774f16-1049088-16cb48903db3ed%22%2C%22%24device_id%22%3A%2216cb48903da31e-047f11eacc848c-48774f16-1049088-16cb48903db3ed%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=492e5f172c33a140bc1282e5db95eccc8944bf6faa55abc96e25ea7f8f7463aa; _putrc=BE08C183E8C0189D123F89F2B170EADC; login=true; unick=%E6%B5%8B%E8%AF%95; gate_login_token=839650030e87ae62992fb24f16361955888990aac080083958ca45634b584ef0; SEARCH_ID=88e8aabc0b184367aeb9844f254aeb18; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=9e31de4b62150c0b1107936651dd4efc9acc2cde96; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566397010; LGRID=20190821221651-523916af-c41e-11e9-8b2f-525400f775ce',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
    }
    def start_requests(self):
        urls = ['https://www.lagou.com/zhaopin/{}/'.format(i) for i in range(1, 31)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        print(response.url)
        for i in response.css('li.con_list_item'):
            salary = i.css('div.p_bot span::text').re('(\d+)k-(\d+)k')
            salary_list = salary if salary else [0, 0]
            experience, education = i.css('div.li_b_l::text').extract()[2].strip().split(' / ')
            experience = re.findall('\d+', experience)
            experience_list = experience if experience else [0, 0]
            experience_list = experience if len(experience) > 1 else [0, 1]
            if len(experience) == 1:
                experience_list = [0, 1]
            yield JobItem(
                title = i.css('h3::text').extract_first(),
                city = i.xpath('.//em/text()').extract_first().split('·')[0],
                salary_low = int(salary_list[0]),
                salary_up = int(salary_list[1]),
                experience_low = int(experience_list[0]),
                experience_up = int(experience_list[1]),
                education = education,
                tags = ' '.join(i.css('div.list_item_bot span::text').extract()),
                company = i.css('div.company a::text').extract_first()
            )
