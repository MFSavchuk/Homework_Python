# -*- coding: utf-8 -*-

from district.central_street.house1 import room1 as s1h1room1
from district.central_street.house1 import room2 as s1h1room2
from district.central_street.house2 import room1 as s1h2room1
from district.central_street.house2 import room2 as s1h2room2

from district.soviet_street.house1 import room1 as s2h1room1
from district.soviet_street.house1 import room2 as s2h1room2
from district.soviet_street.house2 import room1 as s2h2room1
from district.soviet_street.house2 import room2 as s2h2room2

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

people_district = [*s1h1room1.folks, *s1h2room1.folks, *s2h1room1.folks, *s2h2room1.folks, *s1h1room2.folks, *s1h2room2.folks, *s2h1room2.folks, *s2h2room2.folks]

print('На районе живут: ' + ', '.join(people_district))
print(f'Населенеие составляет {len(people_district)} человек ')
print('Населенеие составляет %d человек ' % (len(people_district)))





