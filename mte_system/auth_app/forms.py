from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User_Profile

class UserCreationForm(forms.ModelForm): 

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta: 

        model = User_Profile

        fields = (
            "username", 
            "kuet_id", 
            "first_name", 
            "last_name", 
            "email"
        )
    
    def clean_password2(self): 

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2 : 
            raise ValidationError("Passwords didn't match")

        return password2

    
    def save(self, commit = True): 

        user = super().save(commit=False)

        user.set_password(self.cleaned_data.get("password2"))

        if commit: 
            user.save()

        return user


class UserChangeForm(forms.ModelForm): 

    password = ReadOnlyPasswordHashField()

    class Meta: 
        model = User_Profile
        fields = (
            "kuet_id", 
            "username", 
            "first_name", 
            "last_name", 
            "email", 
            "password"
        )

    def clean_password(self):
        return self.initial["password"]