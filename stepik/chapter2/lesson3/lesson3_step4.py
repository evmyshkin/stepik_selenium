# Задание: принимаем alert https://stepik.org/lesson/184253/step/4?unit=158843

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import re

def calc(x):
    return math.log(abs(12*math.sin(x)))

link_test = "http://suninjuly.github.io/alert_accept.html"
link_stepik = "https://stepik.org/lesson/184253/step/4?unit=158843"

pattern = '\d\d\W\d+'

try:
    browser = webdriver.Chrome()
    browser.get(link_test)
    time.sleep(1)

    btn1 = browser.find_element(By.CLASS_NAME, "btn")
    btn1.click()
    time.sleep(1)

    alert1 = browser.switch_to.alert
    alert1.accept()
    time.sleep(1)

    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    btn2 = browser.find_element(By.CLASS_NAME, "btn")
    btn2.click()
    
    alert2 = browser.switch_to.alert
    alert2_num = alert2.text

    stepik_answer = re.findall(pattern, alert2_num)
    print(stepik_answer[0])


finally:
    browser.quit()
