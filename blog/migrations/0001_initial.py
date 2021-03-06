# Generated by Django 2.2.11 on 2020-04-10 14:21

import blog.models
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, default=None, null=True, unique=True, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=blog.models.image_folder, verbose_name='Фотка')),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит(Не трогать)')),
                ('key_word', models.CharField(blank=True, max_length=120, null=True, verbose_name='Ключевые слова')),
                ('key_descriptin', models.CharField(blank=True, max_length=120, null=True, verbose_name='Мето описани')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Текст')),
                ('description_short', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Текст(короткий)')),
                ('is_active', models.BooleanField(default=True, verbose_name='В наличии')),
                ('top', models.BooleanField(default=False, verbose_name='В топе(на гл.странице)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='blog.Teg', to_field='slug', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статья',
            },
        ),
    ]
