from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, 'num1').text
    number2 = browser.find_element(By.ID, 'num2').text
    result = int(number1) + int(number2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(f'{result}')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
