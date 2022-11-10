# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def triangle(point, angel=0, length=100):
    for x in range(3):
        v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angel = angel + 120


def square(point, angel=0, length=100):
    for x in range(4):
        v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angel = angel + 90


def pentagon(point, angle, length):
    corners = 5
    for count in range(corners):

        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 0:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == corners - 1:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
            return
        angle = angle + (360 / corners)
        point = v1.end_point


def hexagon(point, angle, length=100):
    corners = 6
    for count in range(corners):

        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 0:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == corners - 1:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
            return
        angle = angle + (360 / corners)
        point = v1.end_point


def draw(point, angle, length, corners):
    for count in range(corners):

        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 0:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == corners - 1:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
            return
        angle = angle + (360 / corners)
        point = v1.end_point


# point_0 = sd.get_point(100, 100)
# triangle(point=point_0, angel=10, length=100)
#
# point_1 = sd.get_point(450, 100)
# square(point=point_1, angel=23, length=125)
#
# point_2 = sd.get_point(100, 350)
# pentagon(point=point_2, angle=25, length=100)
#
# point_3 = sd.get_point(350, 350)
# hexagon(point=point_3, angle=33, length=100)

point_4 = sd.get_point(350, 100)
draw(point=point_4, angle=33, length=100, corners=9)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
