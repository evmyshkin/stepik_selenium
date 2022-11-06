# Задание: запуск автотестов для разных языков интерфейса https://stepik.org/lesson/237240/step/10

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: fr, en or es")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "fr":
        print(f"\nStarting browser for testing language {language}")
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': f'{language}'})
        browser = webdriver.Chrome(options=options)
    elif language == "en":
        print(f"\nStarting browser for testing language {language}")
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': f'{language}'})
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        print(f"\nStarting browser for testing language {language}")
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': f'{language}'})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be fr, en or es")
    yield browser
    print("\nQuitting browser")
    browser.quit()
