from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    surname = models.TextField(max_length=50, null=False, blank=False, verbose_name=('Фамилия'))
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name=('Имя'))
    patronymic = models.TextField(max_length=50, null=False, blank=False, verbose_name=('Отчество'))
    city = models.TextField(max_length=100, null=False, blank=False, verbose_name=('Город'))
    phone_number = models.TextField(max_length=12, null=False, blank=True, verbose_name=('Номер телефона'))

def __str__(self):
    return str(self.user)









# Create your models here.
