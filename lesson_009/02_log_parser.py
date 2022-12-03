# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


file = 'events.txt'


class EventCounter:
    def __init__(self, file_name, result_file_name):
        self.result_file_name = result_file_name
        self.file_name = file_name
        self.events = {}

    def analyze_and_result(self):
        with open(self.file_name, mode='r', encoding='utf8') as file_analyze:
            for line in file_analyze:
                self._if_for_counter(line)
        self._result()

    def _if_for_counter(self, line):
        key = line[1:17]
        if 'NOK' in line:
            if key in self.events.keys():
                self.events[key] += 1
            else:
                self.events[key] = 1
        elif key not in self.events.keys():
            self.events[key] = 0

    def _result(self):
        with open(self.result_file_name, 'w', encoding='utf8') as file_result:
            for key, item in self.events.items():
                file_result.write(f'[{key}] {item}\n')


class EventCounterPerHours(EventCounter):
    def _if_for_counter(self, line):
        key = line[1:14]
        if 'NOK' in line:
            if key in self.events.keys():
                self.events[key] += 1
            else:
                self.events[key] = 1
        elif key not in self.events.keys():
            self.events[key] = 0


class EventCounterPerMonth(EventCounter):
    def _if_for_counter(self, line):
        key = line[1:8]
        if 'NOK' in line:
            if key in self.events.keys():
                self.events[key] += 1
            else:
                self.events[key] = 1
        elif key not in self.events.keys():
            self.events[key] = 0


class EventCounterPerYear(EventCounter):
    def _if_for_counter(self, line):
        key = line[1:5]
        if 'NOK' in line:
            if key in self.events.keys():
                self.events[key] += 1
            else:
                self.events[key] = 1
        elif key not in self.events.keys():
            self.events[key] = 0


counter = EventCounter(file_name=file, result_file_name='02_result_per_minutes')
counter.analyze_and_result()

counter_per_hours = EventCounterPerHours(file_name=file, result_file_name='02_result_per_hours')
counter_per_hours.analyze_and_result()

counter_per_month = EventCounterPerMonth(file_name=file, result_file_name='02_result_per_month')
counter_per_month.analyze_and_result()

counter_per_year = EventCounterPerYear(file_name=file, result_file_name='02_result_per_year')
counter_per_year.analyze_and_result()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
