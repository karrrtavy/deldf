# Generated by Django 5.1.5 on 2025-02-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия'),
        ),
    ]
