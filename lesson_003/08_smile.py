# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

sd.resolution = (600, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def draw_smile(color_element=sd.COLOR_YELLOW):
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    left_bottom = sd.get_point(x, y)
    right_top = sd.get_point(x + 150, y + 200)
    sd.ellipse(right_top=right_top, left_bottom=left_bottom, color=color_element, width=2)

    one = sd.get_point(x + 25, y + 80)
    two = sd.get_point(x + 50, y + 60)
    three = sd.get_point(x + 100, y + 60)
    four = sd.get_point(x + 125, y + 80)
    point_list = [one, two, three, four]
    sd.lines(point_list=point_list, color=color_element, width=2)

    center_position1 = sd.get_point(x + 50, y + 125)
    radius = 7
    sd.circle(center_position=center_position1, radius=radius, color=color_element, width=2)

    center_position2 = sd.get_point(x + 100, y + 125)
    sd.circle(center_position=center_position2, radius=radius, color=color_element, width=2)


smiles = input('Введите число смайлов: ')
for _ in range(int(smiles)):
    color = sd.random_color()
    draw_smile(color_element=color)

sd.pause()

# while True:
#     end = input('Введите q для выхода')
#     if end == 'q':
#         exit()
