# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as simple_draw

simple_draw.resolution = (600, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

left_bottom = simple_draw.get_point(-50, 0)
right_top = simple_draw.get_point(50, 50)

for y in range(0, 600, 100):
    for x in range(-50, 650, 100):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
        left_bottom = simple_draw.get_point(x + 50, y + 50)
        right_top = simple_draw.get_point(x + 150, y + 100)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)

simple_draw.pause()
