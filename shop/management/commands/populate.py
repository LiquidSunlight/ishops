from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Product, ProductImage
from PIL import Image, ImageDraw, ImageFont 

import random

class Command (BaseCommand):
    help = "Populates test data"

    def handle(self, *args, **options):

        cat_cnt = 10
        subcat_cnt = 7
        max_depth = 2

        def add_products(cat):
            for n in range(1, random.randint(1, 15)):
                prod = Product.objects.create(name = "Товар {}_{}".format(n, cat.id),
                    slug="tovar_{}_{}".format(n, cat.id), 
                    price = random.randrange(1000,50000)/100,
                    stock = random.randrange(10, 400),
                    category = cat
                    )

                print ("created", prod)

                prod.save()
                for m in range(1, random.randint(1, 3)):
                    img = ProductImage.objects.create(product = prod)
                    im = Image.new('RGB', (640, 480), (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
                    draw = ImageDraw.Draw(im)
                    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
                    draw.text((250,170), "image {}".format(m), font = fnt, fill=(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
                    draw.text((150,220), "product {}".format(prod), font = fnt, fill=(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
                    draw.text((150,270), "category {}".format(cat), font = fnt, fill=(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
                    im.save("products/2018/03/20/img{}p{}.png".format(m, prod.id))
                    img.image = "products/2018/03/20/img{}p{}.png".format(m, prod.id)
                    img.save()


        def add_sub_categories(parent_cat, depth, subcat_cnt):
            depth-=1
            for n in range(1, random.randint(1, subcat_cnt)):
                sub_cat = Category.objects.create(name = "{}_{}".format(parent_cat.name, n),
                    slug = "{}_{}".format(parent_cat.slug, n), parent_category = parent_cat)
                sub_cat.save()
                if random.randint(0,depth):
                    add_sub_categories(sub_cat, depth, subcat_cnt)
                else:
                    add_products(sub_cat)

        for cat in Category.objects.all():
            cat.delete()        

        for c in range(1, cat_cnt):
            new_cat = Category.objects.create(name = "Категория{}".format(c), 
                slug = "kategoriia{}".format(c))
            new_cat.save()
            add_sub_categories(new_cat, max_depth, subcat_cnt)


