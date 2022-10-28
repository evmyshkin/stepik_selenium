# Пример задачи для execute_script https://stepik.org/lesson/228249/step/5?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(2)

# скрипт, скроллящий на 100 пикселей
browser.execute_script("window.scrollBy(0, 100);")
time.sleep(2)

button = browser.find_element(By.TAG_NAME, "button")
# скрипт, скроллящий элемент до видимости
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(2)

button.click()

time.sleep(3)
browser.close()
