# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# Решение:

months = 10
educational_grant_for_alltime = 0

i = 1
while i <= months:
    if i == 1:
        educational_grant_for_alltime = educational_grant_for_alltime + educational_grant
        i += 1
        continue
    educational_grant = educational_grant * 1.03
    educational_grant_for_alltime = educational_grant_for_alltime + educational_grant
    i += 1

expenses_for_alltime = expenses * months
parents_money = round(educational_grant_for_alltime, 2) - expenses * months

if expenses_for_alltime >= educational_grant_for_alltime:
    print('Студенту хватает денег на', months, 'месяцев.', 'Даже остается', round((expenses_for_alltime - educational_grant_for_alltime)), 'рублей')
elif expenses_for_alltime < educational_grant_for_alltime:
    print('На', months, 'месяцев', 'студенту надо попросить', round((educational_grant_for_alltime - expenses_for_alltime)), 'рублей')
