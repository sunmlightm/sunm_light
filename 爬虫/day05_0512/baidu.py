from  selenium import webdriver
from  selenium.webdriver.chrome.options import Options
import time
chrome_options=Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com/')

driver.find_element_by_id("kw").send_keys('尚硅谷')
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(3)

driver.save_screenshot('尚硅谷.png')
driver.quit()