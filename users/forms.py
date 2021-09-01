from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django import forms
from .models import Profile

class Signupform(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), max_length=20, required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput(), max_length=20, required=True)
    class Meta:
        model=User
        fields=["username","email","password"]
    def clean_confirm_password(self):
        print("clean")
        formdata=self.cleaned_data
        print(formdata)
        password = formdata["password"]
        confirm_password = formdata.get("confirm_password")
        if(password!=confirm_password) :
            raise forms.ValidationError("Password do not Match") 


class Loginform(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), max_length=20, required=True)
    class Meta:
        model=User
        fields=["username","email"]
class ProfileUpdateform(ModelForm):
    class Meta:
        model=Profile
        fields=['image']
class UserUpdateForm(ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
