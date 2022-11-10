# -*- coding: utf-8 -*-

from district.central_street.house1 import room1 as s1h1room1
from district.central_street.house1 import room2 as s1h1room2
from district.central_street.house2 import room1 as s1h2room1
from district.central_street.house2 import room2 as s1h2room2

from district.soviet_street.house1 import room1 as s2h1room1
from district.soviet_street.house1 import room2 as s2h1room2
from district.soviet_street.house2 import room1 as s2h2room1
from district.soviet_street.house2 import room2 as s2h2room2

from room_1 import folks as folks_room1
from room_2 import folks as folks_room2


people_room1 = [*s1h1room1.folks, *s1h2room1.folks, *s2h1room1.folks, *s2h2room1.folks, *folks_room1]
people_room2 = [*s1h1room2.folks, *s1h2room2.folks, *s2h1room2.folks, *s2h2room2.folks, *folks_room2]

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...


print('В комнате room_1 живут: ' + ', '.join(people_room1))
print('В комнате room_2 живут: ' + ', '.join(people_room2))
