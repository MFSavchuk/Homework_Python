# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    fallen_flakes = 0

    def __init__(self):
        self.x_cords = sd.random_number(0, 600)
        self.y_cord = sd.random_number(300, 600)
        self.size = sd.random_number(5, 10)
        self.wind = 0
        self.position = None
        self.can_fall_status = True

    def draw(self):
        self.position = sd.get_point(self.x_cords, self.y_cord)
        sd.snowflake(center=self.position, length=self.size, color=sd.COLOR_WHITE)

    def move(self):

        self.wind = sd.random_number(-5, 5)
        self.x_cords -= self.wind
        self.y_cord -= sd.random_number(6, 10)

    def clear_previous_picture(self):
        self.position = sd.get_point(self.x_cords, self.y_cord)
        sd.snowflake(center=self.position, length=self.size, color=sd.background_color)

    def can_fall(self):
        # if not self.can_fall_status:
        #     return self.can_fall_status
        if self.y_cord < 100:
            # self.can_fall_status = False
            Snowflake.fallen_flakes += 1
            # return self.can_fall_status


def get_flakes(count):
    flakes = []
    for _ in range(count):
        flakes.append(Snowflake())
    return flakes


def get_fallen_flakes():
    # count = 0
    # for flake in flakes:
    #     if not flake.can_fall_status:
    #         count += 1
    # print(count)
    print(Snowflake.fallen_flakes)
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

flakes = get_flakes(3)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
    fallen_flakes = Snowflake.fallen_flakes  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
