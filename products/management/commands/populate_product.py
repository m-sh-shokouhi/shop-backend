import random
from django.core.management.base import BaseCommand
from ...models import Product, ProductImage, Category
from faker import Faker
from django.core.files.base import ContentFile

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


class Command(BaseCommand):
    help = 'Description of your command'  # Help text displayed when running `python manage.py help your_command_name`

    def handle(self, *args, **kwargs):
        # Your command logic goes here
        faker = Faker("fa_IR")
        self.stdout.write(self.style.SUCCESS('Creating fake products!'))

        categories = ["بچه‌گانه", "زنانه", "مردانه"]
        for category in categories:
            category = Category.objects.create(
                name=category,
                description="توصیفی در مورد دسته بندی",
                slug=category
            )

        width, height = 300, 200
        product_names = ["جوراب", "لباس", "شلوار", "کفش"]
        category = Category.objects.filter(name="بچه‌گانه")[0]
        for name in product_names:
            product = Product.objects.create(
                name=name,
                category=category,
                slug=name, # It is only one word length
                price=random.randint(100,200)*1000,
                stock=random.randint(1,50),
                description="متن مورد نظر را اینجا قرار دهید"
            )
            
            img = Image.new("RGB", (width, height), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            draw = ImageDraw.Draw(img)
            
            font = ImageFont.truetype("products/management/commands/lalezar.ttf", 30)  # Use a built-in font
            
            bbox = font.getbbox(name)
            text_width = bbox[2] - bbox[0]  # Width of the text
            text_height = bbox[3] - bbox[1]  # Height of the text
            x = (width - text_width) / 2
            y = (height - text_height) / 2

            # Step 5: Draw the text on the image
            text_color = (0, 0, 0)  # Black
            draw.text((x, y), name, font=font, fill=text_color)
            image_io = BytesIO()
            img.save(image_io, format="PNG")
            

            ProductImage.objects.create(
                product=product,
                image=ContentFile(image_io.getvalue(), name=f"random_{random.randint(1000, 9999)}.png")
            )

        self.stdout.write(self.style.SUCCESS('fake products creation finished!'))