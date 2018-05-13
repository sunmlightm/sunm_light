from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.douban.com/')
time.sleep(1)

driver.find_element_by_id("form_email").send_keys('sunmpa1@163.com')
driver.find_element_by_id('form_password').send_keys('sunm8917')

driver.find_element_by_xpath("//input[@class='bn-submit']").click()
time.sleep(3)

driver.save_screenshot("登录成功.png")
driver.quit()