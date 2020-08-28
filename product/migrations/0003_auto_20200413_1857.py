# Generated by Django 2.2.11 on 2020-04-13 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200405_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brend',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='brend',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brend',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Brend', to_field='name', verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tkan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Tkan', to_field='name', verbose_name='Ткань'),
        ),
        migrations.AlterField(
            model_name='tkan',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tkan',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит'),
        ),
    ]
