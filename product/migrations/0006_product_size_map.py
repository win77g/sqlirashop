# Generated by Django 2.2.11 on 2020-08-27 17:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200529_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_map',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Карта размеров'),
        ),
    ]
