from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    time.sleep(5)
    button.click()

    #переключаемся на другую вкладку
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, 'input_value').text
    input = browser.find_element(By.ID, 'answer')
    result = calc(int(x))
    input.send_keys(str(result))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

