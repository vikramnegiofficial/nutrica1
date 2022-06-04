from dataclasses import field
from secrets import choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from requests import request

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    # email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # email = self.cleaned_data.get('email')

        if username and password:
            user1 = authenticate(username=username, password=password)
            # user2 = authenticate(username=email, password=password)
            if not (user1 ):
                raise forms.ValidationError("User doesn't exist")
            # if not (user1.check_password or user2.check_password):
            #     raise forms.ValidationError("Incorrect Password")
        return super(LoginForm, self).clean(*args, **kwargs)

class RegistrationUser(UserCreationForm):
    email = forms.EmailField(required=True ,max_length=254, help_text='Enter a valid email address')
    first_name = forms.CharField(max_length=100, required=True, help_text='Optional')
    mobile = forms.IntegerField(required=True , max_value=9999999999)

    choicesAccount=[
        ("patient", "patient"),
        ("hospital staff", "hospital staff")
    ]
    last_name = forms.ChoiceField(choices=choicesAccount)  #account(choices=choicesAccount)
    choiceGender = [
        ("male", "male"),
        ("female", "female"),
    ]
    gender = forms.ChoiceField(choices=choiceGender)

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'mobile', 
            'email', 
            'last_name',
            'gender',
            'password1', 
            'password2', 
            ]