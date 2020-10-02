from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="sign_in")
def profile_dash(request): 
    return render(request, "profile_app/dash.html")
