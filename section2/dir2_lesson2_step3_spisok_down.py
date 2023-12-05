from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    url = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(url)

    num1_elt = browser.find_element(By.ID, 'num1')
    num1 = int(num1_elt.text)

    num2_elt = browser.find_element(By.ID, 'num2')
    num2 = int(num2_elt.text)

    sum_nums = str(num1 + num2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(sum_nums)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
