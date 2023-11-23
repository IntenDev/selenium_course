import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(url)
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element(By.LINK_TEXT, text)
link.click()

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ilya")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Kosterin")
input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("Moscow")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()