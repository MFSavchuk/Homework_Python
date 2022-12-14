# -*- coding: utf-8 -*-

import os, time, shutil, zipfile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов:)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

path = 'C:\\Users\\michael\\OneDrive\\Desktop\\icons'
path_zip = 'icons.zip'
new_path = 'C:\\Users\\michael\\OneDrive\\Desktop\\icons_by_year'

class FilesArrange:

    def __init__(self, path, new_path):
        self.path = os.path.normpath(path)
        self.new_path = os.path.normpath(new_path)

    # Пройтись по всем файлам в директории.

    def arrange(self):
        for dirpath, dirnames, filenames in os.walk(self.path):

            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                time_file = time.gmtime(secs)
                full_new_path = os.path.join(self.new_path, str(time_file.tm_year), str(time_file.tm_mon))

                if os.path.isdir(full_new_path):
                    shutil.copy2(full_file_path, full_new_path)
                else:
                    os.makedirs(full_new_path)
                    shutil.copy2(full_file_path, full_new_path)


filesarrange = FilesArrange(path=path, new_path=new_path)
filesarrange.arrange()

# with zipfile.ZipFile(path_zip, 'a') as zf:
#     for file in zf.namelist():
#         print(file)
#         # print(os.path.dirname(file))
#
#         if file.endswith('.png'):
#
#             # full_file_path = os.path.join(dirpath, file)
#             secs = os.path.getmtime(file)
#             # time_file = time.gmtime(secs)
#             # full_new_path = os.path.join(self.new_path, str(time_file.tm_year), str(time_file.tm_mon))
#             #
#             # if os.path.isdir(full_new_path):
#             #     shutil.copy2(full_file_path, full_new_path)
#             # else:
#             #     os.makedirs(full_new_path)
#             #             shutil.copy2(full_file_path, full_new_path)

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
