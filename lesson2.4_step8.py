from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    is_price_100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    book_button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    book_button.click()

    x = browser.find_element(By.ID, 'input_value').text
    input = browser.find_element(By.ID, 'answer')
    result = calc(int(x))
    input.send_keys(str(result))

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

