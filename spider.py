import json
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

results = []

def parse(response):
    for comment in response.css('div.comment-item'):
        result = {}
        result['name'] = comment.css('div.user-name a::text').extract_first().strip()
        result['content'] = comment.css('div.content::text').extract_first().strip()        
        results.append(result)

def has_next_page(response):
    class_value = response.xpath('//ul[@class="pagination"]/li[2]/@class').extract_first().strip()
    if "disabled" in class_value:
        return True
    else:
        return False

def goto_next_page(driver):
    ac = driver.find_element_by_xpath('(//li[contains(@class, "page-item")])[2]')
    ActionChains(driver).move_to_element(ac).perform()
    time.sleep(1)
    ac.click()

def wait_page_return(driver, page):
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
        )
    )

def spider():
    driver = webdriver.PhantomJS()
    # driver = webdriver.Firefox()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)

    # while True:
    #     wait_page_return(driver, page)
    #     html = driver.page_source
    #     response = HtmlResponse(url=url, body=html.encode('utf8'))
    #     parse(response)        
    #     if not has_next_page(response):
    #         break          
    #     goto_next_page(driver)
       
    while True:
        time.sleep(3)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        parse(response)
        if has_next_page(response):
            break
        goto_next_page(driver)       


    with open('/home/shiyanlou/comments.json', 'w') as f:
        f.write(json.dumps(results))

if __name__ == '__main__':
    spider()
