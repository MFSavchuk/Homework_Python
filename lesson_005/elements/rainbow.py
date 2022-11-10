import simple_draw as sd


def draw_rainbow(point, radius):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    for color in rainbow_colors:
        sd.circle(center_position=point, radius=radius, width=20, color=color)
        radius += 20
