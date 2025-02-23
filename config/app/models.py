from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    surname = models.CharField(max_length=30, blank=True, verbose_name=('Фамилия'))
    name = models.CharField(max_length=20, blank=True, verbose_name=('Имя'))
    patronymic = models.CharField(max_length=30,blank=True, verbose_name=('Отчество'))
    city = models.CharField(max_length=30,blank=True, verbose_name=('Город'))
    phone_number = models.CharField(max_length=12, blank=True, unique=True, null=True, verbose_name=('Номер телефона'))

def save(self, *args, **kwargs):
        if self.pk:
            original = UserProfile.objects.get(pk=self.pk)
            if original.phone_number:
                if self.phone_number != original.phone_number:
                    raise ValidationError('Вы не можете изменить номер телефона.')
            if original.surname:
                if self.surname != original.surname:
                    raise ValidationError('Вы не можете изменить номер телефона.')
            if original.name:
                if self.name != original.name:
                    raise ValidationError('Вы не можете изменить номер телефона.')
            if original.patronymic:
                if self.patronymic != original.patronymic:
                    raise ValidationError('Вы не можете изменить номер телефона.')
            if original.city:
                if self.city != original.city:
                    raise ValidationError('Вы не можете изменить номер телефона.')
        super().save(*args, **kwargs)

def __str__(self):
    return f"{self.user.username}"
# Create your models here.