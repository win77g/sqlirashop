# Generated by Django 2.2.11 on 2020-06-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20200602_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasketmodel',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Итого'),
        ),
    ]
