# Conftest.py и передача параметров в командной строке https://stepik.org/lesson/237240/step/7?unit=209628

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print(f"\nStarting {browser_name} for a test")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print(f"\nStarting {browser_name} for a test")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuitting browser")
    browser.quit()