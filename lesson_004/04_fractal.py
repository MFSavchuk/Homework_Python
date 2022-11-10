# -*- coding: utf-8 -*-

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# def draw_bunches(start_point, angle, length):
#     if length < 3:
#         return
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle - 30, length=length * .75)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 30, length=length * .75)
#     v3.draw()
#     draw_bunches(start_point=v2.end_point, angle=angle - 30, length=length * .75)
#     draw_bunches(start_point=v3.end_point, angle=angle + 30, length=length * .75)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# pip install simple_draw - Установка


import simple_draw as sd

sd.resolution = (800, 600)
sd.background_color = sd.COLOR_BLACK


def draw_bunches_start(start_point, angle, length):
    sd.start_drawing()  # закоментировать строку, если нужено видеть процесс рисования
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=4)
    v1.draw(color=sd.COLOR_DARK_GREEN)

    delta_angle = sd.random_number(21, 42)
    delta_length = (sd.random_number(6, 9)) / 10
    angle_1 = angle - delta_angle
    angle_2 = angle + delta_angle
    length = length * delta_length

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle_1,
                       length=length, width=4)
    v2.draw(color=sd.COLOR_DARK_GREEN)

    v3 = sd.get_vector(start_point=v1.end_point, angle=angle_2,
                       length=length, width=4)
    v3.draw(color=sd.COLOR_DARK_GREEN)

    draw_bunches_continuation(start_point=v2.end_point, angle=angle_1, length=length)
    draw_bunches_continuation(start_point=v3.end_point, angle=angle_2, length=length)
    sd.finish_drawing()  # закоментировать строку, если нужено видеть процесс рисования


def draw_bunches_continuation(start_point, angle, length):
    if length < 2:
        return

    delta_angle = sd.random_number(21, 42)
    delta_length = (sd.random_number(6, 9)) / 10
    angle_1 = angle - delta_angle
    angle_2 = angle + delta_angle
    length = length * delta_length

    v2 = sd.get_vector(start_point=start_point, angle=angle_1,
                       length=length)
    v2.draw(color=sd.random_color())

    v3 = sd.get_vector(start_point=start_point, angle=angle_2,
                       length=length)
    v3.draw(color=sd.random_color())

    draw_bunches_continuation(start_point=v2.end_point, angle=angle_1, length=length)
    draw_bunches_continuation(start_point=v3.end_point, angle=angle_2, length=length)


root_point = sd.get_point(400, -50)
draw_bunches_start(start_point=root_point, angle=90, length=120)

sd.pause()
