import simple_draw as sd


def draw_triangle(point, angel=0, length=100):


    for x in range(3):
        v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angel = angel + 120


def draw_point():
    point = sd.get_point(300, 300)
    sd.circle(center_position=point, radius=1)
