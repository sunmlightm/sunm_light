# _*_coding:utf-8_*_
# Author : sunm
# @Time :  18:23
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
    return text


def get_product_info():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    soup=BeautifulSoup(driver.page_source,'lxml')
    item_list = soup.select('#mainsrp-itemlist .items .item')
    for items in item_list:
        item_dict={}
        item_dict['price']=items.select('.price strong')[0].text
        item_dict['location'] = items.select('.location')[0].text
        item_dict['shop']=items.select('.shop')[0].text.strip()
        item_dict['image'] ='https:'+ items.select('.J_ItemPic.img')[0].attrs["data-src"]
        item_dict['title'] = items.select('a[class="J_ClickStat"]')[0].text.strip()
        item_dict['product_link']='https:'+items.select('a[class="J_ClickStat"]')[0].attrs["href"]
# price(价格)，location(销售地)，shop(商店名称)，image(图片)，title(商品名称)，product_link商品连接
        print(item_dict)


def next_page(page):
    print("当前正在加载第%s页的数据" % page)
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div > input")))
        input.clear()
        input.send_keys(page)
        driver.find_element_by_css_selector("#mainsrp-pager > div > div > div > div > span.btn.J_Submit").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul.items > li.item.active"), str(page)))
    except Exception as e:
        next_page(page)
    get_product_info()
def main():
    page_num = get_pages()
    get_product_info()
    for page in range(2,int(page_num)+1):
        next_page(page)
    driver.quit()
if __name__ == '__main__':
    main()
