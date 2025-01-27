from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Departament, Category, products, ProductImage


# Register your models here.

class CategoryInline(admin.StackedInline):
    model = Category
    extra = 0


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)
    inlines = [
        CategoryInline
    ]


class imageInlines(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'slug', 'description', 'price', 'quantity', 'discount', 'weight', 'type_product', 'category')
    inlines = [
        imageInlines
    ]

    def get_image(self, product):
        images = product.productsimage_set.all()
        if images:
            return mark_safe(f'<img src="{images[0], images.url}" width="100"')
        return ''
