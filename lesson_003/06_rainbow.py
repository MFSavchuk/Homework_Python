# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (600, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x1 = 50
x2 = 350

for color in rainbow_colors:
    start_point = sd.get_point(x1, 50)
    end_point = sd.get_point(x2, 450)
    x1 += 10
    x2 += 10
    sd.line(start_point=start_point, end_point=end_point, color=color, width=10)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

sd.clear_screen()

radius = 800
point = sd.get_point(400, -150)
for color in rainbow_colors:
    point = sd.get_point(400, -500)
    sd.circle(center_position=point, radius=radius, width=20, color=color)
    radius += 20

sd.pause()
