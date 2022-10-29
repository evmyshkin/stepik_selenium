# Задание: Про Exceptions https://stepik.org/lesson/181384/step/6?unit=156009

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "button")

finally:
    browser.quit()
