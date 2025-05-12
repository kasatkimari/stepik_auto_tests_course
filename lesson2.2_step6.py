from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/execute_script.html'
def calc(x):
    return math.log(12 * math.sin(x))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    y = Calc(int(x))

    #вводим ответ в поле ввода
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    #ставим чекбокс
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # ставим радиобаттон
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    # скроллим вниз
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

