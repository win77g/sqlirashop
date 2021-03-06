# Generated by Django 2.2.11 on 2020-06-13 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detskoePostelnoe', '0002_auto_20200602_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Тип',
            },
        ),
        migrations.AddField(
            model_name='detskapostel',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='detskoePostelnoe.Type', to_field='name', verbose_name='Тип'),
        ),
    ]
