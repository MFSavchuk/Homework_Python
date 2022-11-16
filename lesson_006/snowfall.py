import simple_draw as sd

_holder = []


def create_snowflakes(count):
    for i in range(count):
        random_x = sd.random_number(0, 600)
        random_y = sd.random_number(600, 1200)
        random_size = sd.random_number(5, 10)

        _holder.append([random_x, random_y, random_size])


def draw_snowflakes(color):
    sd.start_drawing()

    for i in range(len(_holder)):
        center_point = sd.get_point(_holder[i][0], _holder[i][1])
        sd.snowflake(center=center_point, length=_holder[i][2], color=color)

    sd.finish_drawing()


def move_snowflakes():
    for i in range(len(_holder)):
        wind = sd.random_number(-5, 5)
        _holder[i][0] -= wind
        _holder[i][1] -= sd.random_number(6, 10)


def check_falls_snowflakes():
    numbers_fallen_snowflakes = []
    for i in range(len(_holder)):
        if _holder[i][1] < sd.random_number(-5, 10):
            numbers_fallen_snowflakes.append(i)
    numbers_fallen_snowflakes.sort(reverse=True)

    for i in numbers_fallen_snowflakes:
        _holder.pop(i)
    create_snowflakes(len(numbers_fallen_snowflakes))
