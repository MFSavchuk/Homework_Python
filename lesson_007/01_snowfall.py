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
        if self.y_cord < 0:
            Snowflake.fallen_flakes += 1


def get_flakes(count):
    flakes_1 = []
    for _ in range(count):
        flakes_1.append(Snowflake())
    return flakes_1


def get_fallen_flakes():
    print(Snowflake.fallen_flakes)
    return Snowflake.fallen_flakes


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())
    # Snowflake.fallen_flakes = 0


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
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
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
