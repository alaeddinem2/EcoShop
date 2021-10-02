# Generated by Django 2.1.4 on 2021-09-03 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatName', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('CatSlug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('CatName',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrdName', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('PrdSlug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('PrdImage', models.ImageField(blank=True, upload_to='products/', verbose_name='Image')),
                ('PrdDescription', models.TextField(blank=True, verbose_name='Description')),
                ('PrdPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('PrdOldPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Old Price')),
                ('PrdStock', models.PositiveIntegerField(verbose_name='Stock')),
                ('PrdAvailable', models.BooleanField(default=True, verbose_name='Available')),
                ('PrdCreated', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('PrdUpdated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('PrdCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-PrdCreated',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'PrdSlug')},
        ),
    ]