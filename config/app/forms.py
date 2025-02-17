from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .cities import CITIES



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
        return user



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['surname', 'name', 'patronymic', 'city', 'phone_number']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form_control'}),
            'name': forms.TextInput(attrs={'class': 'form_control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form_control'}),
            'city': forms.TextInput(attrs={'class': 'form_control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form_control', 'type': 'number'})            
        }

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city not in CITIES:
            raise forms.ValidationError('Указанный город отсутствует в списке городов нашей системы')
        return city




    



