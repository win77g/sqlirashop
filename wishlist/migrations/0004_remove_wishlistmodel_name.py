# Generated by Django 2.2.11 on 2020-04-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_auto_20200412_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='name',
        ),
    ]