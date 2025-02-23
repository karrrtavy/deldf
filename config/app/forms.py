from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .cities import CITIES
from django.core.exceptions import ValidationError



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Пользователь с таким адресом уже зарегистрирован.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            UserProfile.objects.get_or_create(user=user)
        return user



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['surname', 'name', 'patronymic', 'city', 'phone_number']
        widgets = {
            'surname': forms.TextInput(attrs={'minlength': 3, 'maxlength': 30}),
            'name': forms.TextInput(attrs={'minlength': 3, 'maxlength': 20}),
            'patronymic': forms.TextInput(attrs={'minlength': 2, 'maxlength': 30}),
            'city': forms.TextInput(attrs={'maxlength': 30}),
            'phone_number': forms.TextInput(attrs={'maxlength': 11})
        }     

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError('Поле номера телефона не может быть пустым.')
        phone_number = phone_number.strip()
        if phone_number.startswith('8'):
            phone_number = '+7' + phone_number[1:]
        if not phone_number.startswith('+7'):
            raise forms.ValidationError("Номер должен начинаться с '+7'.")
        if len(phone_number) != 12:
            raise forms.ValidationError("Номер телефона должен содержать 12 символов (включая '+').")
        if not phone_number[1:].isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры после '+'.")
        if UserProfile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Этот номер телефона уже используется')
        return phone_number
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            if self.instance.phone_number:
                self.fields['phone_number'].widget.attrs['readonly'] = True
            if self.instance.city:
                self.fields['city'].widget.attrs['readonly'] = True
            if self.instance.surname:
                self.fields['surname'].widget.attrs['readonly'] = True
            if self.instance.name:
                self.fields['name'].widget.attrs['readonly'] = True
            if self.instance.patronymic:
                self.fields['patronymic'].widget.attrs['readonly'] = True

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city not in CITIES:
            raise forms.ValidationError('Указанный город отсутствует в списке городов нашей системы')
        return city
