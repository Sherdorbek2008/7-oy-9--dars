from django.db import models


# Create your models here.

class Departament(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='nomi')
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='departament/images/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='nomi')
    slug = models.SlugField(max_length=150, unique=True)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


TypeProduct = {
    "kg": "kg",
    "l": "l"
}


class products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='nomi')
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(null=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=10)
    discount = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    type_product = models.CharField(max_length=2, choices=TypeProduct)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/images/')
    products = models.ForeignKey(products, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name
