from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    button = browser.find_element(By.TAG_NAME, "button")
    button_disabled = button.get_attribute("disabled")
    assert button_disabled is None

    time.sleep(12)
    button_disabled = button.get_attribute("disabled")
    assert button_disabled is not None, "Button is not disabled"

finally:
    browser.quit()
