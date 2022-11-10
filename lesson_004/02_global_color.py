# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw(point, angle, length, corners, color=sd.COLOR_YELLOW):
    for count in range(corners):
        if count == 0:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == corners - 1:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, color=color, width=3)
            return
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)
        angle = angle + (360 / corners)
        point = v1.end_point


point_4 = sd.get_point(350, 100)


while True:
    print('Введите вариант:')
    print('1 - RED, 2 - ORANGE, 3 - YELLOW, 4 - GREEN, 5 - CYAN, 6 - BLUE, '
          '7 - COLOR_PURPLE')
    var = input()
    color = sd.COLOR_YELLOW
    if var == '1':
        color = sd.COLOR_RED
        break
    elif var == '2':
        color = sd.COLOR_ORANGE
        break
    elif var == '3':
        color = sd.COLOR_YELLOW
        break
    elif var == '4':
        color = sd.COLOR_GREEN
        break
    elif var == '5':
        color = sd.COLOR_CYAN
        break
    elif var == '6':
        color = sd.COLOR_BLUE
        break
    elif var == '7':
        color = sd.COLOR_PURPLE
        break
    else:
        print('Ошибка ввода !!! Повторите')

corners = 3
while True:
    print('Введите вариант:')
    print('3 - Треугольник, 4 - Квадрат, 5 - Пятиугольник, 6 - Шестиугольник')
    var = input()
    if var == '3':
        corners = 3
        break
    elif var == '4':
        corners = 4
        break
    elif var == '5':
        corners = 5
        break
    elif var == '6':
        corners = 6
        break
    else:
        print('Ошибка ввода!!!')


draw(point=point_4, angle=33, length=100, corners=corners, color=color)

sd.pause()
