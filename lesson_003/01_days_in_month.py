# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

if month == 1:
    month_name = 'Январь'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 2:
    month_name = 'Февраль'
    days = 28
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 3:
    month_name = 'Март'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 4:
    month_name = 'Апрель'
    days = 30
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 5:
    month_name = 'Май'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 6:
    month_name = 'Июнь'
    days = 30
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 7:
    month_name = 'Июль'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 8:
    month_name = 'Август'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 9:
    month_name = 'Сентябрь'
    days = 30
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 10:
    month_name = 'Октябрь'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 11:
    month_name = 'Ноябрь'
    days = 30
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
elif month == 12:
    month_name = 'Декабрь'
    days = 31
    print('Вы ввели', month, 'месяц по счету:', month_name, '\n', 'Дней в нем:', days)
else:
    print('Всего 12 месяцев! Вы ввели некорректный номер месяца!')
