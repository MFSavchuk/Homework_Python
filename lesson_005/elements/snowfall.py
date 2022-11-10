import simple_draw as sd


def draw_snowfall(x_start, x_stop):
    N = 25  # количество снежинок
    x_cords = []  # координаты x
    y_cords = []  # координаты y
    sizes = []  # размеры снежинок
    factor_a = []
    factor_b = []
    factor_c = []
    count = 0  # счетчик для увеличения сугроба

    while True:
        if count > 150:
            sd.pause()
            break

        for i in range(N):
            random = sd.random_number(x_start, x_stop)
            x_cords.append(random)

            random = sd.random_number(200, 300)
            y_cords.append(random)

            random = sd.random_number(2, 5)
            sizes.append(random)

            random = float((sd.random_number(50, 70)) / 100)
            factor_a.append(random)

            random = float((sd.random_number(20, 40)) / 100)
            factor_b.append(random)

            random = sd.random_number(55, 65)
            factor_c.append(random)

        while True:
            sd.start_drawing()
            if max(y_cords) < 200:
                if count > 10:
                    count -= 1
                    break
                else:
                    count += 1
                    break

            for i in range(len(y_cords)):
                if y_cords[i] < 10 + count:
                    center_point = sd.get_point(x_cords[i], y_cords[i])
                    sd.snowflake(center=center_point, length=sizes[i], color=sd.COLOR_WHITE, factor_a=factor_a[i],
                                 factor_b=factor_b[i], factor_c=factor_c[i])
                    continue

                center_point = sd.get_point(x_cords[i], y_cords[i])
                sd.snowflake(center=center_point, length=sizes[i], color=sd.background_color, factor_a=factor_a[i],
                             factor_b=factor_b[i], factor_c=factor_c[i])
                y_cords[i] -= sd.random_number(6, 10)
                wind = sd.random_number(-5, 5)
                x_cords[i] -= wind
                center_point = sd.get_point(x_cords[i], y_cords[i])
                sd.snowflake(center=center_point, length=sizes[i], color=sd.COLOR_WHITE, factor_a=factor_a[i],
                             factor_b=factor_b[i], factor_c=factor_c[i])

            sd.finish_drawing()
            sd.sleep(0.1)
            if sd.user_want_exit():
                break
