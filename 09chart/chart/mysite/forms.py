from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=20)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
