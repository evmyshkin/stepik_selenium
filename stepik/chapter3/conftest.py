# Conftest.py — конфигурация тестов https://stepik.org/lesson/237240/step/2?unit=209628
# Применяются по очереди все conftest.py с корневой папки до папки с целевым тестом. 
# Поэтому стоит убрать для разных директорий их conftest.py в параллельные папки и не хранить общий conftest.py в корневой.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
