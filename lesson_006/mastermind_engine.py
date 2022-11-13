import random as rd

hidden_number = []


def get_number():
    global hidden_number
    while True:
        if len(hidden_number) == 4:
            break
        random = rd.randint(1, 9)
        if random in hidden_number:
            continue
        else:
            hidden_number.append(random)


def check_number():
    pass
