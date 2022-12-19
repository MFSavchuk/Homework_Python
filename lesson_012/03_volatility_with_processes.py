# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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
import os
from collections import defaultdict
from lesson_012.python_snippets.utils import time_track
import multiprocessing


class Analyzer(multiprocessing.Process):

    def __init__(self, path, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.ticker = None
        self.volatility = None
        self.collector = collector

    def run(self):
        with open(self.path, 'r', encoding='utf8') as ff:
            price_list = []

            for line in ff:
                line = line[:-1]
                secid, tradetime, price, quantity = line.split(',')
                # with self.lock:
                #     print(secid, tradetime, price, quantity)
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

        self.collector.put(dict(ticker=self.ticker, volatility=self.volatility))


def print_result(tickers_volatility):
    tickers_zero_volatility = defaultdict(lambda: float)
    tickers_not_zero_volatility = defaultdict(lambda: float)

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
def my_func(path):
    collector = multiprocessing.Queue()
    analyzers = [Analyzer(path=os.path.join(dirpath, file), collector=collector) for
                 dirpath, dirnames, filenames in os.walk(path)
                 for file in filenames]
    for analyzer in analyzers:
        analyzer.start()
    for analyzer in analyzers:
        analyzer.join()

    tickers_volatility = defaultdict(lambda: float)
    while not collector.empty():
        data = collector.get()
        tickers_volatility[data['ticker']] = data['volatility']

    print_result(tickers_volatility=tickers_volatility)


my_path = 'trades'
if __name__ == '__main__':
    my_func(path=my_path)
