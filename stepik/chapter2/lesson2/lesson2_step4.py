# Метод execute_script https://stepik.org/lesson/228249/step/4?unit=200781

from selenium import webdriver

browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")
browser.close()
