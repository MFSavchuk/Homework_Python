import simple_draw as sd


def draw_bunches_start(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=4)
    v1.draw(color=sd.COLOR_DARK_GREEN)

    delta_angle = sd.random_number(21, 42)
    delta_length = (sd.random_number(6, 9)) / 10
    angle_1 = angle - delta_angle
    angle_2 = angle + delta_angle
    length = length * delta_length

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle_1,
                       length=length, width=4)
    v2.draw(color=sd.COLOR_DARK_GREEN)

    v3 = sd.get_vector(start_point=v1.end_point, angle=angle_2,
                       length=length, width=4)
    v3.draw(color=sd.COLOR_DARK_GREEN)

    draw_bunches_continuation(start_point=v2.end_point, angle=angle_1, length=length)
    draw_bunches_continuation(start_point=v3.end_point, angle=angle_2, length=length)


def draw_bunches_continuation(start_point, angle, length):
    if length < 2:
        return

    delta_angle = sd.random_number(21, 42)
    delta_length = (sd.random_number(6, 9)) / 10
    angle_1 = angle - delta_angle
    angle_2 = angle + delta_angle
    length = length * delta_length

    v2 = sd.get_vector(start_point=start_point, angle=angle_1,
                       length=length)
    v2.draw(color=sd.random_color())

    v3 = sd.get_vector(start_point=start_point, angle=angle_2,
                       length=length)
    v3.draw(color=sd.random_color())

    draw_bunches_continuation(start_point=v2.end_point, angle=angle_1, length=length)
    draw_bunches_continuation(start_point=v3.end_point, angle=angle_2, length=length)


