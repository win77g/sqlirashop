# Generated by Django 2.2.11 on 2020-04-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_remove_wishlistmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistmodel',
            name='product_name',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Продукт'),
        ),
    ]