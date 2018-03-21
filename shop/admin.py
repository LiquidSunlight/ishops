from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.

#Модель категории товаров
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Изображения товара
class ProductImageInline(admin.TabularInline):
    model = ProductImage    
# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [ProductImageInline,]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
