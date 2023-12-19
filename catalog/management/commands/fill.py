from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()


        categories = [
            {'name': 'Стратегии', 'discription': 'Описание стратегии'},
            {'name': 'Ролевые игры', 'discription': 'Описание ролевых игр'},
            {'name': 'Шутеры', 'discription': 'Описание шутеров'},
        ]

        products = [
            {'name': 'Warhammer 40000', 'category_id': 1, 'price': 1000, 'discription': 'Описание игры'},
            {'name': 'Counter-Strike', 'category_id': 3, 'price': 500, 'discription': 'Описание игры'},
            {'name': 'Titan Quest', 'category_id': 2, 'price': 700, 'discription': 'Описание игры'},
        ]

        for category in categories:
            Category.objects.create(**category)

        for product in products:
            Product.objects.create(**product)
