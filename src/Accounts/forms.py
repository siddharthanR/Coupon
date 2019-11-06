from django import forms
from .models import Register

class RegisterForm(forms.Form):
	name = forms.CharField(max_length = 50)
	age = forms.IntegerField()
	email = forms.EmailField(max_length = 50)
	city = forms.CharField(max_length = 25)
	referalcode = forms.CharField(required=False, max_length = 7)
	referalany = forms.CharField(required=False, max_length = 7)