# Задание: переход на новую вкладку https://stepik.org/lesson/184253/step/6?unit=158843

import math
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return math.log(abs(12*math.sin(x)))

pattern = '\d\d\W\d+'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    troll_btn = browser.find_element(By.CLASS_NAME, "trollface")
    troll_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit_btn = browser.find_element(By.CLASS_NAME, "btn")
    submit_btn.click()

    alert = browser.switch_to.alert
    alert_num = alert.text

    stepik_answer = re.findall(pattern, alert_num)
    print(stepik_answer[0])

finally:
    browser.quit()
