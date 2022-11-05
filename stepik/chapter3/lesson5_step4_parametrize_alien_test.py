# Задание: параметризация тестов https://stepik.org/lesson/237240/step/4?unit=209628

import pytest
import time
import math
from selenium.webdriver.common.by import By

email = "cccc"
password = "bbbb!"
expected_feedback_message = "Correct!"


@pytest.fixture(scope='function')
def authorization(browser):
    authorisation_link = "https://stepik.org/catalog?auth=login"
    browser.get(authorisation_link)
    browser.implicitly_wait(15)

    email_input = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    email_input.send_keys(email)

    password_input = browser.find_element(
        By.CSS_SELECTOR, '#id_login_password')
    password_input.send_keys(password)

    login_button_modal = browser.find_element(
        By.CSS_SELECTOR, '.sign-form__btn')
    login_button_modal.click()

    browser.implicitly_wait(15)
    browser.find_element(By.CSS_SELECTOR, '.navbar__profile-img')


@pytest.fixture(scope='function')
def task_reset(browser):
    yield task_reset
    reset_button = browser.find_element(By.CSS_SELECTOR, '.again-btn')
    reset_button.click()

    browser.find_element(By.CSS_SELECTOR, '.submit-submission:disabled')


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answer_math_time(browser, lesson, authorization, task_reset):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)

    textarea = browser.find_element(By.TAG_NAME, "textarea")

    answer = math.log(int(time.time()))

    browser.implicitly_wait(15)
    textarea.send_keys(answer)

    btn = browser.find_element(By.CLASS_NAME, "submit-submission")
    browser.implicitly_wait(15)
    btn.click()

    actual_feedback_message = browser.find_element(
        By.CLASS_NAME, "smart-hints__hint").text
    assert actual_feedback_message == expected_feedback_message, f'Actual feedback was "{actual_feedback_message}"'
