# Generated by Django 2.2.11 on 2020-04-12 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200405_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('image', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', to_field='name', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Товар в жиланиях',
                'verbose_name_plural': 'Товары в жиланиях',
            },
        ),
    ]
