from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_image = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
    x = treasure_image.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
