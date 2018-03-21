from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Product, ProductImage

class Command (BaseCommand):
    help = "Cleans test data"

    def handle(self, *args, **options):
        for cat in Category.objects.all():
            cat.delete()        
