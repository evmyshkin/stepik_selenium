# Проект с авто-тестами с курса Stepik «Автоматизация тестирования с помощью Selenium и Python»

## Подготовка к использованию проекта в среде MacOS
1. Установить python 3.6 и выше:[Python.org](https://www.python.org/downloads/)
2. Склонировать проект в нужную директорию
`$ git clone https://github.com/evmyshkin/stepik_selenium/`
3. Добавить виртуальное окружение Python в склонированный проект
`$ python3 -m venv stepik_selenium`
4. Активировать виртуальное окружение, указав актуальный путь
`$ source /../../../stepik_selenium/bin/activate`
5. Установить зависимости для проекта
`$ pip install -r requirements.txt`
6. Скачать Selenium Webdriver, соответствующий версии браузера
7. Распаковать драйвер по адресу 
`$ sudo mv chromedriver /usr/local/bin`
8. Проверить версию драйвера, ответ укажет, что установка успешна:
`$ chromedriver -v`
