# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)



# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

import simple_draw as sd

from lesson_005.elements.rainbow import draw_rainbow
from lesson_005.elements.tree import draw_bunches_start as draw_tree
from lesson_005.elements.snowfall import draw_snowfall
from lesson_005.elements.sun import draw_sun

sd.resolution = (1500, 700)
sd.background_color = (78, 187, 253)

sd.start_drawing()

sun_start_point = sd.get_point(200, 550)
draw_sun(sun_start_point=sun_start_point)

rainbow_start_point = sd.get_point(750, -500)
rainbow_radius = 1000
draw_rainbow(point=rainbow_start_point, radius=rainbow_radius)

tree_start_point = sd.get_point(1200, -50)
draw_tree(start_point=tree_start_point, angle=90, length=100)

draw_snowfall(x_start=200, x_stop=450)

sd.finish_drawing()
sd.pause()
