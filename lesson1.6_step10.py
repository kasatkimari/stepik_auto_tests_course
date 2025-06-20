from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
	link = "http://suninjuly.github.io/registration2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	input_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
	input_name.send_keys("Ivan")
	input_last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
	input_last_name.send_keys("Petrov")
	input_email = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='email']")
	input_email.send_keys("nnn@mail.ru")
	# плюс необязательные
	#input_phone = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='phone']")
	#input_phone.send_keys("34534543")
	#input_address = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='address']")
	#input_address.send_keys("baker street")

	# Отправляем заполненную форму
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)

	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text

	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()