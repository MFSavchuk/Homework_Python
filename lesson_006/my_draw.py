from my_draw_engine import draw_triangle, draw_point
import simple_draw as sd

start_point = sd.get_point(100, 100)

draw_triangle(point=start_point, length=400)
draw_point()

sd.pause()