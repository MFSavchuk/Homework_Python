# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# for item in goods:
#     article = store[goods[item]]
#     items_quantity = 0
#     items_total_cost = 0
#     for position_in_warehouse in article:
#         items_quantity += position_in_warehouse['quantity']
#         items_cost = position_in_warehouse['price'] * position_in_warehouse['quantity']
#         items_total_cost += items_cost
#     print(item, '-', items_quantity, 'шт, общая стоимость', items_total_cost, 'руб.')


for item, article in goods.items():
    items_quantity = 0
    items_total_cost = 0
    for position_in_warehouse in store[article]:
        items_quantity += position_in_warehouse['quantity']
        items_cost = position_in_warehouse['price'] * position_in_warehouse['quantity']
        items_total_cost += items_cost
    print(item, '-', items_quantity, 'шт, общая стоимость', items_total_cost, 'руб.')
