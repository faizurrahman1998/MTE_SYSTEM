from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User_Profile
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin): 

    #for updating user 
    form = UserChangeForm

    #for adding a new user 
    add_form = UserCreationForm

    #which fields are shown in admin panel
    list_display = (
        "username", 
        "first_name", 
        "last_name", 
        "isSuperuser"
    )

    #which fields are used to filter the `user_profile` data
    list_filter = (
        "username", 
        "kuet_id"
    )

    #fields needed for changing the user informations 

    fieldsets = (
        (None, {
            "fields": ("username", "password")
        }), 
        ("Personal_info", {
            "fields": ("first_name", "last_name", "email")
        }), 
        ("Permissions", {
            "fields": ("isStaff", "isSuperuser", "isActive")
        })
    )

    #fields needed while creating a user 
    add_fieldsets = (
        (None, {
            "classes" : ("wide"), 
            "fields" : ("kuet_id", "username", "first_name", "last_name", "email", "password1", "password2")
        }),
    )

    search_fields = (
        "username",
        "kuet_id",
    )

    ordering = (
        "username",
        "kuet_id" 
    )

    filter_horizontal = ()

admin.site.register(User_Profile, UserAdmin)


