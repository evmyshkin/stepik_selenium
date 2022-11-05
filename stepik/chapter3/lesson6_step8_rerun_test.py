# Плагины и перезапуск тестов https://stepik.org/lesson/237240/step/8?unit=209628

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
    
    # запустить тест с параметром для перезапуска падающего теста
    # pytest -v --tb=line --reruns 1 lesson6_step8_rerun_test.py