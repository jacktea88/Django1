from django import forms
from mysite import models
# for order form
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=20)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = models.Profile
#         fields = ['height', 'male', 'website']

#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         self.fields['height'].label = '身高(cm)'
#         self.fields['male'].label = '是男生嗎'
#         self.fields['website'].label = '個人網站'

# for order form
class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = ['full_name', 'address', 'phone']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = '收件人姓名'
        self.fields['address'].label = '郵寄地址'
        self.fields['phone'].label = '聯絡電話'