from django.core.management.base import BaseCommand
from ...models import Product, ProductImage, Category
from faker import Faker
class Command(BaseCommand):
    help = 'Description of your command'  # Help text displayed when running `python manage.py help your_command_name`

    def handle(self, *args, **kwargs):
        # Your command logic goes here
        faker = Faker("fa_IR")
        self.stdout.write(self.style.SUCCESS('Deleteing models'))

        Category.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Finish Deleting'))