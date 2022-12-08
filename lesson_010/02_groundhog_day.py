# -*- coding: utf-8 -*-
import random


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    karma = random.randint(1, 7)
    dice_1 = random.randint(1, 13)
    if dice_1 == 6:
        dice_2 = random.choice(['IamGod', 'Drunk', 'CarCrash', 'Gluttony', 'Depression', 'Suicide'])
        if dice_2 == 'IamGod':
            raise IamGodError('Я бог')
        if dice_2 == 'Drunk':
            raise DrunkError('Умер от перебуха')
        if dice_2 == 'CarCrash':
            raise CarCrashError('Разбился на авто')
        if dice_2 == 'Gluttony':
            raise GluttonyError('Объелся и умер')
        if dice_2 == 'Depression':
            raise DepressionError('Умер от дипресии')
        if dice_2 == 'Suicide':
            raise SuicideError('Сошерщил самоубийсвто')
    return karma


ENLIGHTENMENT_CARMA_LEVEL = 777
karma = 0

while karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma += one_day()
        print(karma)
    except Exception as exc:
        with open('karma.txt', 'a', encoding='utf8') as ff:
            ff.write(f'Случилось - {exc}\n')

# https://goo.gl/JnsDqu
