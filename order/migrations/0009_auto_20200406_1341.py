# Generated by Django 2.2.11 on 2020-04-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20200406_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasketmodel',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Продукт'),
        ),
    ]
