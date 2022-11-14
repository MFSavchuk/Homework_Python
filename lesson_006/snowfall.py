import simple_draw as sd

snowflakes = []
numbers_fallen_snowflakes = []


def create_snowflakes(count):
    for i in range(count):
        random_x = sd.random_number(0, 600)
        random_y = sd.random_number(600, 1200)
        random_size = sd.random_number(25, 50)

        snowflakes.append([random_x, random_y, random_size])


def draw_snowflakes(color):
    sd.start_drawing()

    for i in range(len(snowflakes)):
        center_point = sd.get_point(snowflakes[i][0], snowflakes[i][1])
        sd.snowflake(center=center_point, length=snowflakes[i][2], color=color)

    sd.finish_drawing()


def move_snowflakes():
    for i in range(len(snowflakes)):
        wind = sd.random_number(-5, 5)
        snowflakes[i][0] -= wind
        snowflakes[i][1] -= sd.random_number(6, 10)


def check_falls_snowflakes():
    global numbers_fallen_snowflakes
    numbers_fallen_snowflakes = []
    for i in range(len(snowflakes)):
        if snowflakes[i][1] < -100:
            numbers_fallen_snowflakes.append(i)
    numbers_fallen_snowflakes.sort(reverse=True)

    for i in numbers_fallen_snowflakes:
        snowflakes.pop(i)
    create_snowflakes(len(numbers_fallen_snowflakes))
