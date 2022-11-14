# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf

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

sf.create_snowflakes(125)

while True:
    sf.draw_snowflakes(sd.background_color)
    sf.move_snowflakes()
    sf.draw_snowflakes(sd.COLOR_WHITE)
    sf.check_falls_snowflakes()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
