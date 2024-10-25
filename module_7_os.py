from os import path, walk
from time import  strftime, localtime

directory = '.'
for root, dirs, files in walk(directory):
    for file in files:
        filepath = path.join(root, file)
        filetime = path.getctime(filepath)
        formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
        filesize = path.getsize(filepath)
        parent_dir = path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
