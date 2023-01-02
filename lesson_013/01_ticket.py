# -*- coding: utf-8 -*-
import os

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


from PIL import Image, ImageDraw, ImageFont


def make_ticket(fio, from_, to, date):
    fio = fio.upper()
    from_ = from_.upper()
    to = to.upper()
    date = date.upper()

    template_path = os.path.join('images', 'ticket_template.png')
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype('arialmt.ttf', size=14)
    draw.text((43, 133), fio, font=font, fill='#000000', )
    draw.text((43, 201), from_, font=font, fill='#000000', )
    draw.text((43, 266), to, font=font, fill='#000000', )
    draw.text((285, 266), date, font=font, fill='#000000', )

    template.save('my_ticket.png')
    # template.show()


make_ticket(fio='Савчук М.Ф.', from_='Астана', to='Москва', date='31.01')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
