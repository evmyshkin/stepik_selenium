# Задание: запуск автотестов для разных языков интерфейса https://stepik.org/lesson/237240/step/10

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_language(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form .btn')