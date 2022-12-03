# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile

file = 'python_snippets/voyna-i-mir.txt.zip'


class CounterValuesDown:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stats = {}
        self.sorted_stats = None
        self.sorted_tuple = None

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stats.keys():
                            self.stats[char] += 1
                        else:
                            self.stats[char] = 1
        self._stats_sorted()
        self._stats_print()

    def _stats_sorted(self):
        self.sorted_tuple = sorted(self.stats.items(), reverse=True, key=lambda x: x[1])

    def _stats_print(self):
        self.sorted_stats = dict(self.sorted_tuple)

        print('+{a:-^10}+{b:-^10}+'.format(a='-', b='-'))
        print('|{a:^10}|{b:^10}|'.format(a='буква', b='частота'))
        print('+{a:-^10}+{b:-^10}+'.format(a='-', b='-'))

        for key, item in self.sorted_stats.items():
            print('|{:^10}|{:^10}|'.format(key, item))
        print('+{a:-^10}+{b:-^10}+'.format(a='-', b='-'))
        print('|{a:^10}|{b:^10}|'.format(a='итого', b=sum(self.sorted_stats.values())))
        print('+{a:-^10}+{b:-^10}+'.format(a='-', b='-'))


class CounterValuesUp(CounterValuesDown):
    def _stats_sorted(self):
        self.sorted_tuple = sorted(self.stats.items(), reverse=False, key=lambda x: x[1])


class CounterKeysUp(CounterValuesDown):
    def _stats_sorted(self):
        self.sorted_tuple = sorted(self.stats.items(), reverse=False, key=lambda x: x[0])


class CounterKeysDown(CounterValuesDown):
    def _stats_sorted(self):
        self.sorted_tuple = sorted(self.stats.items(), reverse=True, key=lambda x: x[0])


counter = CounterKeysDown(file_name=file)
counter.collect()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
