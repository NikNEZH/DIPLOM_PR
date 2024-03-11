from django.core.management.base import BaseCommand
from recipes_app.models import Category


class Command(BaseCommand):
    help = 'Creat new categories'

    def handle(self, *args, **options):
        # Create random category
        category_1 = Category(title='Супы', theme='На обед')
        category_2 = Category(title='Гарниры', theme='На обед')
        category_3 = Category(title='Выпечка', theme='На десерт')
        category_4 = Category(title='Мороженное', theme='На ужин')

        category_1.save()
        category_2.save()
        category_3.save()
        category_4.save()