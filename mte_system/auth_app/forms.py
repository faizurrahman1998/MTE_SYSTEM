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

    def clean_email(self): 

        email = self.cleaned_data.get("email")

        if email.split("@")[1] != "stud.kuet.ac.bd": 
            raise ValidationError(f"Domain error.")

        return email
    
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

    class Meta: 
        model = User_Profile

        fields = ( 
            "first_name", 
            "last_name", 
            "image",
        )

    def clean_image(self):

        if self.cleaned_data["image"]: 
            try: 
                name = self.cleaned_data["image"].name
                name = name.replace(name.rsplit(".", 1)[0], "".join(list(self.cleaned_data["first_name"].split(" "))))
                self.cleaned_data["image"].name = name
            except: 
                pass

        return self.cleaned_data["image"]


