import random

from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from .models import *


class Index(ListView):
    model = Departament
    template_name = 'departamenent_list.html'
    context_object_name = "departments"
    paginate_by = 3
    ordering = ["-name"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        product = products.objects.all()
        context['products'] = random.sample(list(product), min(8, len(product))) if product else []
        return context


class Products(ListView):
    model = products
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_queryset(self):
        departament_slug = self.request.GET.get('departament', None)

        if departament_slug:
            departament = get_object_or_404(Departament, slug=departament_slug)
            product = products.objects.filter(category__departament=departament)
        else:
            product = products.objects.all()
        if len(product) >= 8:
            product_list = random.sample(list(product), 8)
        else:
            product_list = product

        return product_list


class Wishlist(View):
    def get(self, request):
        product = products.objects.all()
        return render(request, 'wishlist.html', {'products': product})


class About(View):
    def get(self, request):
        return render(request, 'about.html')