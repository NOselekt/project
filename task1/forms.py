from django import forms

class UserRegister(forms.Form):
    name = forms.CharField(max_length=30, label="Ваше имя")
    age = forms.IntegerField(max_value=150, label="Ваш возраст")
    password = forms.CharField(min_length=8, label="Пароль")
    repeat_password = forms.CharField(min_length=8, label="Повтор пароля")