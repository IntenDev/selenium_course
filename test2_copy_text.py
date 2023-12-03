from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = 'https://www.salon-love-forever.ru/wedding/gabbiano/avrora/'
    browser = webdriver.Chrome()
    browser.get(url)

    x_elt = browser.find_element(By.TAG_NAME, 'h1')
    x = x_elt.text

    price_elt = browser.find_element(By.CSS_SELECTOR, ".product_price_splash strong")
    price = price_elt.text
    print(x + ' ' + '-' + ' ' + price)

finally:
    time.sleep(5)
    browser.quit()



