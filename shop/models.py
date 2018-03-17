from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=200, blank=False, null=False, db_index=True, unique=True)
    parent_category = models.ForeignKey('self', related_name='subcategories',
        verbose_name="Категория", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
        
