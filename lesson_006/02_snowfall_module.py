# -*- coding: utf-8 -*-

import simple_draw as sd

sd.background_color = sd.COLOR_BLACK

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()





N = 25  # количество снежинок
x_cords = []  # координаты x
y_cords = []  # координаты y
sizes = []  # размеры снежинок
factor_a = []
factor_b = []
factor_c = []
count = 0  # счетчик для увеличения сугроба

while True:
    if count > 600:
        print('Завалило весь экран')
        sd.pause()
        break

    for i in range(N):
        random = sd.random_number(0, 600)
        x_cords.append(random)

        random = sd.random_number(600, 1200)
        y_cords.append(random)

        random = sd.random_number(25, 50)
        sizes.append(random)

        random = float((sd.random_number(50, 70)) / 100)
        factor_a.append(random)

        random = float((sd.random_number(20, 40)) / 100)
        factor_b.append(random)

        random = sd.random_number(55, 65)
        factor_c.append(random)

    while True:
        sd.start_drawing()
        if max(y_cords) < 700:
            count += 17
            break

        for i in range(len(y_cords)):
            if y_cords[i] < 10 + count:
                center_point = sd.get_point(x_cords[i], y_cords[i])
                sd.snowflake(center=center_point, length=sizes[i], color=sd.COLOR_WHITE, factor_a=factor_a[i],
                             factor_b=factor_b[i], factor_c=factor_c[i])
                continue

            center_point = sd.get_point(x_cords[i], y_cords[i])
            sd.snowflake(center=center_point, length=sizes[i], color=sd.background_color, factor_a=factor_a[i],
                         factor_b=factor_b[i], factor_c=factor_c[i])
            y_cords[i] -= sd.random_number(6, 10)
            wind = sd.random_number(-5, 5)
            x_cords[i] -= wind
            center_point = sd.get_point(x_cords[i], y_cords[i])
            sd.snowflake(center=center_point, length=sizes[i], color=sd.COLOR_WHITE, factor_a=factor_a[i],
                         factor_b=factor_b[i], factor_c=factor_c[i])

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break