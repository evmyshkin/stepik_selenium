# Задание: ждем нужный текст на странице https://stepik.org/lesson/181384/step/8?unit=156009

import math
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

pattern = '\d\d\W\d+'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


book_button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

book_button.click()

input_value = browser.find_element(By.ID, "input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)

y = calc(int(input_value.text))

answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(y)

submit_button = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

alert = browser.switch_to.alert
alert_answer = alert.text

stepik_answer = re.findall(pattern, alert_answer)
print(stepik_answer[0])