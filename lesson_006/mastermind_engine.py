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


def check_number(guess_number):
    cows = 0
    bulls = 0

    for i in range(len(guess_number)):
        if guess_number[i] == hidden_number[i]:
            bulls += 1
        elif guess_number[i] in hidden_number:
            cows += 1
        else:
            print(f'Число {guess_number[i]} нет в списке')

    print(f'Быки - {bulls}, Коровы - {cows}')
