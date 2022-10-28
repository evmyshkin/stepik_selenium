# Загрузка файлов https://stepik.org/lesson/228249/step/7?unit=200781

import os 

# путь до директории текущего файла
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к пути имя файла 
file_path = os.path.join(current_dir, 'file.txt') 

# передаем элементу путь до файла на загрузку
# element.send_keys(file_path)

# вывести путь до текущего файла
print(os.path.abspath(__file__))

# вывести путь до директории текущего файла
print(os.path.abspath(os.path.dirname(__file__)))

# вывести путь до директории и указанного в file_path файла в ней
print(file_path)