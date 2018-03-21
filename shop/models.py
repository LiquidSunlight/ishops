from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=200, blank=False, null=False, db_index=True, unique=True)
    parent_category = models.ForeignKey('self', related_name='subcategories',
        verbose_name="Категория", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
        
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", 
        on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', verbose_name="Товар", 
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, 
        verbose_name="Изображение товара")

    class Meta:
        ordering = ['product']
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
     