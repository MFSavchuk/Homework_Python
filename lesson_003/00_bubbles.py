# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step, color = sd.COLOR_YELLOW):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


#
point = sd.get_point(100, 300)
bubble(point=point, step=5)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1001, 100):
    point = sd.get_point(x, 200)
    bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(200):
    point = sd.random_point()
    step = random.randint(2, 10)
    color = sd.random_color()
    bubble(point=point, step=step, color=color)

sd.pause()
