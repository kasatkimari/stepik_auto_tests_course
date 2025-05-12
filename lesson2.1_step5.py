from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    #вводим ответ в поле для ввода
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    #ставим чекбокс
    option = browser.find_element(By.ID, 'robotCheckbox')
    option.click()

    #ставим радиобаттон
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()

    #нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

