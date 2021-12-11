from django.db import models

class Category(models.Model):
    name            = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name            = models.CharField(max_length=120)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE) # clave foranea... relaciona tabla products con la de categories
    description     = models.TextField(blank=True, null=True)
    price           = models.FloatField()
    image           = models.ImageField(upload_to='%Y-%m-%d', max_length=None, default='image-placeholder.png', blank=True)

    def __str__(self):
        return self.name