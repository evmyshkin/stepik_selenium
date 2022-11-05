# Запуск автотестов для разных языков интерфейса https://stepik.org/lesson/237240/step/9?unit=209628

""" from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option(
    'prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
 """