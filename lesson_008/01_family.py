# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.total_money = 0
        self.total_food = 0
        self.total_buy_fur_coat = 0
        self.total_money += self.money
        self.cat_food = 30

    def __str__(self):
        return f'{self.name}: денег - {self.money}, еды - {self.food}, кошачей еды - {self.cat_food}, ' \
               f'загрязнен на {self.dirt}%'


class Man:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.happiness = 100
        self.free_days = 0
        self.isAlive = True

    def __str__(self):
        return f'{self.name}: сытость - {self.fullness}, счастье - {self.happiness}'

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 30
            self.house.food -= 30
            self.house.dirt += 5
            self.house.total_food += 30
            print(f'{self.name} покушал(а)')
        else:
            self.fullness -= 5
            print(f'{self.name} голодает...')

    def petting_cat(self):
        self.happiness += 5
        self.fullness -= 10
        self.house.dirt += 5
        print(f'{self.name} гладил(а) кота весь день')


class Husband(Man):

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер от голода...')
            self.isAlive = False
            return
        if self.happiness < 10:
            print(f'{self.name} умер от депрессии...')
            self.isAlive = False
            return
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness < 30:
            self.eat()
        elif self.house.money < 250:
            self.work()
        elif self.happiness < 30:
            chose = randint(1, 5)
            if chose == 1:
                self.coding()
            else:
                self.petting_cat()
        else:
            self.fullness -= 10
            print(f'{self.name} отдыхал')
            self.free_days += 1

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        self.house.total_money += 150
        print(f'{self.name} работал весь день')

    def coding(self):
        self.happiness += 20
        self.fullness -= 10
        self.house.dirt += 5
        print(f'{self.name} программировал весь день')

    def help_wife_with_money(self):
        if self.isAlive:
            self.work()
        else:
            print(f'{self.name} не может это сделать. Он умер...')


class Wife(Man):

    def __init__(self, name, house, helper):
        self.helper = helper
        super().__init__(name=name, house=house)

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умерла от голода...')
            self.isAlive = False
            return
        if self.happiness < 10:
            print(f'{self.name} умерла от депрессии...')
            self.isAlive = False
            return
        if self.house.dirt > 70:
            self.happiness -= 10
        if self.house.food < 30:
            self.shopping()
        if self.happiness < 40:
            self.buy_fur_coat()
        elif self.fullness < 30:
            self.eat()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.dirt > randint(50, 100):
            self.clean_house()
        else:
            chose = randint(1, 5)
            if chose == 1:
                self.petting_cat()
            else:
                self.fullness -= 10
                print(f'{self.name} отдыхала')
                self.free_days += 1

    def shopping(self):
        if self.house.money >= 50:
            self.house.food += 50
            self.house.money -= 50
            self.fullness -= 10
            print(f'{self.name} купила еды')
        else:
            print(f'{self.name} просит {self.helper.name} заработать на еду')
            self.helper.help_wife_with_money()

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.house.total_buy_fur_coat += 1
            print(f'{self.name} купила ШУБУ')
        else:
            print(f'{self.name} просит {self.helper.name} заработать на ШУБУ')
            self.helper.help_wife_with_money()

    def clean_house(self):
        random = randint(5, 100)
        if random <= self.house.dirt:
            self.house.dirt -= random
            self.fullness -= 10
            print(f'{self.name} убиралась весь день')
        else:
            self.house.dirt = 0
            self.fullness -= 10
            print(f'{self.name} убиралась весь день')

    def buy_cat_food(self):
        if self.house.money >= 30:
            self.house.cat_food += 30
            self.house.money -= 30
            self.fullness -= 10
            print(f'{self.name} купила еды для кота')
        else:
            print(f'У {self.name} нет денег на еду коту')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.isAlive = True

    def __str__(self):
        return f'{self.name}: сытость - {self.fullness}'

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер от голода...')
            self.isAlive = False
            return
        chose = randint(1, 9)
        if self.fullness < 20:
            self.eat()
        elif chose == 3:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.fullness += 20
        else:
            self.fullness -= 1
            print(f'{self.name} голодает...')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} спал весь день')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        print(f'{self.name} весь день драл обои')


class Child(Man):

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умерла от голода...')
            self.isAlive = False
            return
        if self.fullness < 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            self.house.dirt += 1
            self.house.total_food += 10
            print(f'{self.name} покушал(а)')
        else:
            self.fullness -= 2
            print(f'{self.name} голодает...')

    def sleep(self):
        self.fullness -= 3
        print(f'{self.name} спал весь день')


home = House(name='Экодолье Шолохово')
misha = Husband(name='Миша', house=home)
lena = Wife(name='Лена', house=home, helper=misha)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    misha.act()
    lena.act()
    kolya.act()
    murzik.act()
    cprint(misha, color='cyan')
    cprint(lena, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

cprint('====================================', color='red')
print(f'{misha.name} отдыхал {misha.free_days} дней')
print(f'{lena.name} отдыхала {lena.free_days} дней')
print(f'Итоги года: съели еды - {home.total_food}, заработали денег - {home.total_money}, купили - '
      f'{home.total_buy_fur_coat} шуб')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживания случайностей моделирование за год делать 3 раза, если 2 из 3-х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
