from django.core.management import BaseCommand

from catalog.models import Category


catalog = [
    'Электроника',
    'Одежда, обувь и аксессуары',
    'Транспорт',
    'Хобби и спорт',
    'Животные и растения',
    'Красота и здоровье',
    'Дом и сад',
    'Строительство и ремонт',
    'Оборудование и сырье',
    'Работа',
    'Недвижимость',
    'Детские товары',
    'Услуги и бизнес',
    'Продукты питания'
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load catalog . . .')
        Category.objects.all()
        for i in catalog:
            c = Category()
            c.name = i
            c.save()
        print('Upload done!')
