from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    # вводим ответ в поле для ввода
    input = driver.find_element(By.ID, 'answer')
    input.send_keys(y)

    # ставим чекбокс
    option = driver.find_element(By.ID, 'robotCheckbox')
    option.click()

    # ставим радиобаттон
    option2 = driver.find_element(By.ID, 'robotsRule')
    option2.click()

    # нажимаем кнопку
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    driver.quit()



