# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class House:

    def __init__(self):
        self.name = 'Экодолье Шолохово'
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'В доме осталось: еды - {}, еды для питомцев - {}, денег - {}. Дом грязный на {} %'.format(
            self.food, self.pet_food, self.money, self.dirt)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 20:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 20
        else:
            cprint('{} ГОЛОДАЕТ !!!'.format(self.name), color='green')
            self.fullness -= 1
            self.shopping()

    def work(self):
        cprint('{} сходил(а) на работу'.format(self.name), color='blue')
        self.house.money += 20
        self.fullness -= 10

    def watch_TV(self):
        cprint('{} смотрел(а) TV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def clean(self):
        if self.fullness > 30:
            cprint('{} убиралась(ся) целый день'.format(self.name), color='green')
            self.house.dirt -= 80
            self.fullness -= 10
        else:
            self.eat()

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил(а) в магазин за едой для {pet.name}', color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def shopping_pet(self):
        if self.house.money >= 50:
            cprint('{} сходил(а) в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.pet_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        if self.name == 'Лена':
            cprint(f'{self.name} въехала в {self.house.name}', color='cyan')
        elif self.name == 'Миша':
            cprint(f'{self.name} въехал в {self.house.name}', color='cyan')

    def take_dog(self, pets_list):
        for pet in pets_list:
            if self.name == 'Лена':
                pet.house = self.house
                pet.name = input('Какой имя дать псу? ')
                print(f'Я {self.name}, и я приютила {pet.name}')
                setattr(self.house, 'pet_food', 0)
                setattr(self.house, 'dirt', 0)


    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.pet_food < 10:
            self.shopping_pet()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt >= 100:
            self.clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_TV()


class Pet:
    def __init__(self):
        self.name = None
        self.house = None
        self.fullness = 20

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.pet_food < 10:
            cprint('{} ГОЛОДАЕТ !!!'.format(self.name), color='green')
            self.fullness -= 2
        else:
            cprint('{} Покушал'.format(self.name), color='green')
            self.fullness += 20
            self.house.pet_food -= 20

    def sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shitting(self):
        cprint('{} гадил и лаял'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)

        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.shitting()


citizens = [
    Man(name='Лена'),
    Man(name='Миша'),
]

pets = [
    Pet(), Pet()
]

my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for citisen in citizens:
    citisen.take_dog(pets)

for day in range(1, 365):
    print('================ день {} ================'.format(day))
    for citisen in citizens:
        citisen.act()
    for pet in pets:
        pet.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for pet in pets:
        print(pet)
        print()
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
