# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw(point, angle, length):
        end_point = point
        for count in range(n):
            if count == n - 1:
                sd.line(start_point=point, end_point=end_point, width=3)
                return
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw()
            angle += (360 / n)
            point = v1.end_point

    return draw


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
