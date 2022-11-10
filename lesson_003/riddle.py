list_nechet = []
list_chet = []

i = -1
while i < 99:
    i += 2
    list_nechet.append(i)
print('Нечетные числа:', list_nechet)

k = 0
while k < 98:
    k += 2
    list_chet.append(k)
print('Четные числа:', list_chet)

count = 0

while True:
    sum_number = list_nechet[0] + list_nechet[-2]
    if len(list_nechet) == 2:
        break
    if sum_number > 98:
        break
    print('Монета', list_nechet[0], 'руб. + Монета -', list_nechet[-2], 'руб. = Монета -', sum_number, 'руб.')
    list_nechet.remove(list_nechet[0])
    list_nechet.remove(list_nechet[-2])
    count += 1

print('Оставшиеся нечетные числа:', list_nechet)
print('Количество конвертаций:', count, 'шт.')
print('Количество нечетных чисел:', len(list_nechet), 'шт.')
