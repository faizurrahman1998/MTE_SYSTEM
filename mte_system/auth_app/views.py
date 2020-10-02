from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm

def sign_up(request): 
    if not request.user.is_authenticated:

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

    else: 
        return redirect("dash")

def sign_in(request): 
    if not request.user.is_authenticated:
        
        if request.method == "POST":

            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user: 
                login(request, user)
                return redirect("dash")
            
            else: 
                messages.error(request, "Username or password is incorrect")
                return render(request, 'auth_app/sign_in.html')

        return render(request, 'auth_app/sign_in.html')
    
    else: 
        return redirect("dash")


def log_out(request): 
    
    logout(request)
    return redirect("sign_in")