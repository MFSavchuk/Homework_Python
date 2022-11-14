import random as rd

hidden_number = []
bulls = None


def get_number():
    global hidden_number
    hidden_number = []
    while True:
        if len(hidden_number) == 4:
            break
        random = rd.randint(0, 9)
        if random in hidden_number:
            continue
        else:
            hidden_number.append(random)
            if hidden_number[0] == 0:
                hidden_number.pop(0)


def check_number(guess_number):
    cows = 0
    global bulls
    bulls = 0

    for i in range(len(guess_number)):
        if guess_number[i] == hidden_number[i]:
            bulls += 1
        elif guess_number[i] in hidden_number:
            cows += 1

    print(f'быки - {bulls}, коровы - {cows}')
