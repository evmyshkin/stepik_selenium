# Conftest.py и передача параметров в командной строке https://stepik.org/lesson/237240/step/7?unit=209628

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
