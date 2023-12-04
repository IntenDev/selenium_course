from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

url = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(url)

try:

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    x_sign = x_element.get_attribute('valuex')
    x = x_sign
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
