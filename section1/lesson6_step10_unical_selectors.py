from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняю поля формы
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys('Ilya')

    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    input2.send_keys("Kosterin")

    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    input3.send_keys("123@mail.ru")

    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.first")
    input4.send_keys('+71231234567')

    input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.second")
    input5.send_keys('Moscow')

    #Отправляю форму

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    # ждем загрузку страницы
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
    welcome_text = welcome_text_elt.text

    # проверяем на совпадение
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()


