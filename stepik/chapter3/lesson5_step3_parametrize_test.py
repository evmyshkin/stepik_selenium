# Параметризация тестов https://stepik.org/lesson/237240/step/3?unit=209628

import pytest
from selenium.webdriver.common.by import By


# параметризация на уровне функции
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


""" также можно применить параметризацию на уровне класса
@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(browser, language):
        ...
    этот тест запустится 2 раза
    
    def test_guest_should_see_navbar_element( browser, language):
    этот тест тоже запустится дважды """
