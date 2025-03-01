# Generated by Django 5.1.4 on 2025-01-17 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='nomi')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('image', models.ImageField(upload_to='departament/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='nomi')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.departament')),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='nomi')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('description', models.TextField(null=True, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=10)),
                ('discount', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('type_product', models.CharField(choices=[('kg', 'kg'), ('l', 'l')], max_length=2)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
        ),
    ]
