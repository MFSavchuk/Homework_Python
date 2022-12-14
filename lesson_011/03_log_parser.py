# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def groupedEvents(file):
    with open(file, 'r', encoding='utf8') as ff:
        prev_time = None
        noc_count = 0

        for line in ff:
            if 'NOK' in line:
                time = line[1:17]
                if time != prev_time:
                    if prev_time is not None:
                        yield prev_time, noc_count

                    prev_time = time
                    noc_count = 0

                noc_count += 1

        if noc_count > 0:
            yield prev_time, noc_count


for group_time, event_count in groupedEvents('events.txt'):
    print(f'[{group_time}] {event_count}')
