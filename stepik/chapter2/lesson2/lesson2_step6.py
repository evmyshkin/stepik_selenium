# Задание на execute_script https://stepik.org/lesson/228249/step/6?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)

    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.close()
