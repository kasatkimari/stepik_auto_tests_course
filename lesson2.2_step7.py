from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Ivan')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Petrov')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('123@test.ru')

    #загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

