# Задание: загрузка файла https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ы")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Ы")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("123@123.123")

    file_button = browser.find_element(By.ID, "file")
    file_button.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.close()