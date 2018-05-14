from selenium import webdriver
import time
import base64
from PIL import Image
from pytesseract import image_to_string

driver = webdriver.Chrome()

def login():
    driver.get("https://www.zhihu.com/signup?next=%2F")
    time.sleep(1)
    driver.find_element_by_css_selector('.SignContainer-switch span').click()
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("trygf521@126.com")
    driver.find_element_by_name("password").send_keys("afu123456")
    if driver.page_source.find("Captcha-englishContainer") != -1:
        print("英文验证码...")
        image = driver.find_element_by_xpath('//div[@class="Captcha-englishContainer"]/img')
        image_data = image.get_attribute("src")
        print(image_data)
        if len(image_data) > len("data:image/jpg;base64,"):
            save_captcha(image_data)
            captcha = get_captcha()
            print("验证码:", captcha)
            driver.find_element_by_name("captcha").send_keys(captcha)
    elif driver.page_source.find("Captcha-chineseContainer") != -1:
        print("中文验证码...")
        image = driver.find_element_by_xpath('//div[@class="Captcha-chineseContainer"]/img')
        print(image.get_attribute("src"))
        image_data = image.get_attribute("src")
        if len(image_data) > len("data:image/jpg;base64,"):
            save_captcha(image_data)
            driver.quit()
    driver.find_element_by_xpath('//div[@class="Login-content"]/form/button').click()
    time.sleep(1)
    driver.save_screenshot("登录成功.png")


def save_captcha(image_data):
    image = image_data[len("data:image/jpg;base64,"):].replace("&#10;", "").replace("%0A", "")
    data_imag = base64.b64decode(image)
    with open("验证码.jpg", "wb") as f:
        f.write(data_imag)
    print("ok...")

def get_captcha():
    try:
        image = Image.open("captcha.jpg")
        text = image_to_string(image)
        print("识别的验证码是:", text)
        cmd = input("是否手动输入验证码y,直接使用识别的验证n:")
        if cmd == "n":
            return text
        elif cmd == "y":
            text = input("请输入验证码:")
            return text
    except Exception as e:
        print("验证码错误")
        text = input("请输入验证码:")
        return text


if __name__ == '__main__':
    login()
    driver.quit()