# Generated by Django 5.1.6 on 2025-02-18 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_profile_id_alter_userprofile_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_id',
        ),
    ]
