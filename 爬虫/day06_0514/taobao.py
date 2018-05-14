from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
chrome_options = Options()
chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options,service_log_path=SERVICE_ARGS)
driver = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(driver, 5)
driver.get('https://www.taobao.com/')


def get_page_num():
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    input.send_keys('美女')
    driver.find_element_by_css_selector('#J_TSearchForm div button').click()
    text = driver.find_element_by_class_name('total').text
    text = re.search(r'\d+', text).group()
    return text


def get_product_info():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    item_list = soup.select('#mainsrp-itemlist .items .item')
    for item in item_list:
        # print('11111111111111111'*10)
        print(item.select('.title')[0].text.strip())


def main():
    page_num = get_page_num()
    print("共计美食:", page_num, '页')
    get_product_info()


if __name__ == '__main__':
    main()
