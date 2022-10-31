# Задание: оформляем тесты в стиле unittest https://stepik.org/lesson/36285/step/13?unit=162401

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
welcome_text_expected = "Congratulations! You have successfully registered!"


class TestAbs(unittest.TestCase):
    def test_welcome_text_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        input1 = browser.find_element(
            By.CSS_SELECTOR, ".form-control[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.CSS_SELECTOR, ".form-control[placeholder='Input your last name']")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(
            By.CSS_SELECTOR, ".form-control[placeholder='Input your email']")
        input3.send_keys("123@ivan.123")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        browser.implicitly_wait(1)

        welcome_text_el = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_el.text

        self.assertEqual(welcome_text_expected, welcome_text,
                         f"Welcome text is different on {browser.current_url}")

    def test_welcome_text_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input1 = browser.find_element(
            By.CSS_SELECTOR, ".form-control[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.CSS_SELECTOR, ".form-control[placeholder='Input your last name']")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(
            By.CSS_SELECTOR, ".form-control[placeholder='Input your email']")
        input3.send_keys("123@ivan.123")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        browser.implicitly_wait(1)

        welcome_text_el = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_el.text

        self.assertEqual(welcome_text_expected, welcome_text,
                         f"Welcome text is different on {browser.current_url}")


if __name__ == "__main__":
    try:
        unittest.main()
    finally:
        browser.quit()
