# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

with open('registrations_good.log', 'w', encoding='utf8') as ff_bad:
    ff_bad.write('')

with open('registrations_bad.log', 'w', encoding='utf8') as ff_bad:
    ff_bad.write('')


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_line(line):
    if len(line) <= 1:
        raise ValueError('Строка пустая')
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise NotNameError('Имя содержит не только буквы')
    if '@' not in email or '.' not in email:
        raise NotEmailError('Почта не содержит @ или . ')
    if not 10 <= int(age) <= 99:
        raise ValueError('Возраст меньше 10 или больше 99')


with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        try:
            check_line(line=line)
            with open('registrations_good.log', 'a', encoding='utf8') as ff_good:
                ff_good.write(line)

        except (ValueError, NotNameError, NotEmailError) as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as ff_bad:
                ff_bad.write(f'{line[:-1]} | Ошибка - "{exc}"\n')
