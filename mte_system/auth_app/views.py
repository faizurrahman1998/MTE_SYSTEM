from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm

def sign_up(request): 

    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            name = form.cleaned_data["first_name"]
            messages.success(request, f"{name} your account was created!")
            return redirect("sign_in")
        
        else: 
            return render(request, "auth_app/sign_up.html", {"errors": form.errors})
    
    return render(request, "auth_app/sign_up.html")


def sign_in(request): 
    return render(request, 'auth_app/sign_in.html')