# -*- coding: utf-8 -*-
import os
from collections import defaultdict
from python_snippets.utils import time_track


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


class AnalyzerFileTransactions:

    def __init__(self, path):
        self.path = path
        self.tickers_volatility = defaultdict(lambda: float)
        self.ticker = None
        self.volatility = None

    def run(self):
        with open(self.path, 'r', encoding='utf8') as ff:
            price_list = []

            for line in ff:
                line = line[:-1]
                secid, tradetime, price, quantity = line.split(',')
                if 'SECID,TRADETIME,PRICE,QUANTITY' in line:
                    continue
                if self.ticker is None:
                    self.ticker = secid
                price = float(price)
                price_list.append(price)

        mix_price = min(price_list)
        max_price = max(price_list)
        average_price = (max_price + mix_price) / 2
        self.volatility = round(((max_price - mix_price) / average_price) * 100, 1)
        print(f'Номер тикера - {self.ticker}, Минимальная цена - {mix_price}, Максимальная цена - {max_price},'
              f'Средняя цена - {average_price}, Волатильность - {self.volatility}%')

        return self.ticker, self.volatility


def print_result(tickers_volatility):
    tickers_zero_volatility = defaultdict(lambda: float)
    tickers_not_zero_volatility = defaultdict(lambda: float)
    tickers_max_volatility = None
    tickers_min_volatility = None

    for ticker, volatility in tickers_volatility.items():
        if volatility == 0:
            tickers_zero_volatility[ticker] = volatility
        else:
            tickers_not_zero_volatility[ticker] = volatility
    tickers_max_volatility = sorted(tickers_not_zero_volatility.items(), key=lambda x: x[1], reverse=True)[:3]
    tickers_min_volatility = sorted(tickers_not_zero_volatility.items(), key=lambda x: x[1], reverse=False)[:3]
    tickers_zero_volatility = sorted(tickers_zero_volatility.items(), key=lambda x: x[0])
    # print(tickers_zero_volatility)
    # print(tickers_min_volatility)
    # print(tickers_max_volatility)
    print('\n')
    print('{a:-^32}'.format(a='-'))
    print('|{a:^30}|'.format(a='Максимальная волатильность:'))
    print('|{a:-^30}|'.format(a='-'))
    for ticker, volatility in tickers_max_volatility:
        print('|{a:^30}|'.format(a=f'ТИКЕР-{ticker} - {volatility} %'))
    print('|{a:-^30}|'.format(a='-'))
    print('|{a:^30}|'.format(a='Минимальная волатильность:'))
    print('|{a:-^30}|'.format(a='-'))
    for ticker, volatility in tickers_min_volatility:
        print('|{a:^30}|'.format(a=f'ТИКЕР-{ticker} - {volatility} %'))
    print('{a:-^32}'.format(a='-'))
    print('{a:^30}'.format(a='Нулевая волатильность:'))
    print('\t', end='')
    for ticker, volatility in tickers_zero_volatility:
        print(f'ТИКЕР-{ticker},', end=' ')
    print('\n')


@time_track
def my_func():
    my_path = 'trades'
    tickers = defaultdict(lambda: float)
    for dirpath, dirnames, filenames in os.walk(my_path):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            my_analyzer = AnalyzerFileTransactions(path=full_file_path)
            ticker, volatility = my_analyzer.run()
            tickers[ticker] = volatility

    print_result(tickers_volatility=tickers)


my_func()
