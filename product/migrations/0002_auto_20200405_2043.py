# Generated by Django 2.2.11 on 2020-04-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Название'),
        ),
    ]