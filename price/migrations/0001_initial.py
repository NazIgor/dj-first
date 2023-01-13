# Generated by Django 4.1.5 on 2023-01-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_title', models.CharField(max_length=30, verbose_name='Название')),
                ('pc_descipt', models.CharField(max_length=256, verbose_name='Описание')),
                ('pc_price', models.CharField(max_length=128, verbose_name='Цена за пакет')),
            ],
            options={
                'verbose_name': 'Пакет',
                'verbose_name_plural': 'Пакеты',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_name', models.CharField(max_length=128, verbose_name='Название')),
                ('pt_old_price', models.CharField(max_length=128, verbose_name='Старая цена')),
                ('pt_price', models.CharField(max_length=128, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
