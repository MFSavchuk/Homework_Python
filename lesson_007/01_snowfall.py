# -*- coding: utf-8 -*-

import simple_draw as sd

sd.background_color = sd.COLOR_BLACK


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    fallen_flakes = 0

    def __init__(self):
        self.x_cords = sd.random_number(0, 600)
        self.y_cord = sd.random_number(600, 1500)
        self.size = sd.random_number(5, 10)
        self.wind = 0
        self.position = None
        self.can_fall_status = True
        self.speed = sd.random_number(5, 10)

    def draw(self):
        self.position = sd.get_point(self.x_cords, self.y_cord)
        sd.snowflake(center=self.position, length=self.size, color=sd.COLOR_WHITE)

    def move(self):
        if self.can_fall():
            self.wind = sd.random_number(-5, 5)
            self.x_cords -= self.wind
            self.y_cord -= self.speed

    def clear_previous_picture(self):
        self.position = sd.get_point(self.x_cords, self.y_cord)
        sd.snowflake(center=self.position, length=self.size, color=sd.background_color)

    def can_fall(self):
        if self.y_cord < sd.random_number(0, 20):
            if self.can_fall_status:
                self.can_fall_status = False
                Snowflake.fallen_flakes += 1
        return self.can_fall_status


def get_flakes(count):
    flakes_list = []
    for _ in range(count):
        flakes_list.append(Snowflake())
    return flakes_list


def get_fallen_flakes():
    return Snowflake.fallen_flakes


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())
    Snowflake.fallen_flakes -= Snowflake.fallen_flakes


# flake = Snowflake()
#
# while True:
#
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

flakes = get_flakes(50)

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
