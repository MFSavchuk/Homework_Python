import simple_draw as sd


def draw_sun(sun_start_point):
    sd.circle(center_position=sun_start_point, radius=100, color=sd.COLOR_YELLOW, width=0)
    for angle in range(0, 360, 27):
        v1 = sd.get_vector(start_point=sun_start_point, angle=angle, length=200, width=2)
        v1.draw(color=sd.COLOR_YELLOW)
