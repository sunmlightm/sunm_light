# _*_coding:utf-8_*_
# Author : sunm
# @Time :  8:29
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()
driver.get('https://www.taobao.com/')
wait = WebDriverWait(driver, 10)

def get_pages():
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
    input.send_keys('美食')
    driver.find_element_by_css_selector('.search-button > button').click()
    text = driver.find_element_by_css_selector('.total').text
    text = re.search(r'\d+', text)[0]
    print(text)
    return text

def get_product_info():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    soup = BeautifulSoup(driver.page_source,'lxml')
    item_list=soup.select('#mainsrp-itemlist .items .item')
    print(item_list)
    for item in item_list:
        item_dict={}
        price = item.select('.price')[0].text
        print(price)


def next_page(page):
    print('当前加载第'+str(page)+"页")
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div div div div input')))
        input.clear()
        input.send_keys(page)
        driver.find_element_by_css_selector('#mainsrp-pager div div div div span.btn').click()
        wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul.items > li.item.active'),str(page))
    except Exception as e:
        print(e)
        next_page(page)
def main():
    page=get_pages()
    get_product_info()
    for page_num in range(2,int(page)+1):
        next_page(page_num)

if __name__ == '__main__':
    main()