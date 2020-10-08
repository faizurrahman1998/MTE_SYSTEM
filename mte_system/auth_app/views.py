from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .utils import activation_token_generator
from .forms import UserCreationForm

def sign_up(request): 

    context = {
        "title" : "Sign Up",
    }

    if not request.user.is_authenticated:

        if request.method == "POST": 
            form = UserCreationForm(request.POST)

            if form.is_valid(): 

                user = form.save(commit=False)
                user.isActive = False

                form.save()

                domain = get_current_site(request).domain
                user_id_64 = urlsafe_base64_encode(force_bytes(user.username))
                token = activation_token_generator.make_token(user)
                activation_url = f'http://{domain}{reverse("verification", kwargs={"uid64": user_id_64, "token": token})}'
                mail_body = render_to_string(
                    "auth_app/verification.html", 
                    context={
                        "name": user.first_name, 
                        "activation_url": activation_url,
                    }
                )

                email = EmailMessage(
                    "Activate your account", 
                    mail_body, 
                    "mteapp.kuet@gmail.com",
                    [user.email]                    
                )
                email.send(fail_silently=False)



                name = user.first_name
                messages.success(request, f"{name} your account was created! Activate it with in 30 mins")
                return redirect("sign_in")
            
            else: 

                context.update({"form": form})
                return render(request, "auth_app/sign_up.html", context)
        
        return render(request, "auth_app/sign_up.html", context=context)

    else: 
        return redirect("dash")


def sign_in(request): 

    context = {
        "title": "Sign in",
    }

    if not request.user.is_authenticated:
        
        if request.method == "POST":

            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user: 
                login(request, user)
                # uid64 = urlsafe_base64_encode(force_bytes(user.username))
                return redirect("dash")
            
            else: 
                messages.error(request, "Username or password is incorrect")
                return render(request, 'auth_app/sign_in.html', context)

        return render(request, 'auth_app/sign_in.html', context)
    
    else: 
        return redirect("dash")



def log_out(request): 
    
    logout(request)
    return redirect("sign_in")


def verification(request, uid64, token):

    user_name = force_text(urlsafe_base64_decode(uid64)) 
    user = get_user_model().objects.filter(username=user_name).first()

    if activation_token_generator.check_token(user, token): 


        user.isActive = True
        user.save()

        login(request, user)

        messages.success(request, "Your Account is acctivated.")
        return redirect("dash")
    
    else: 
        print(user_name, user.isActive)
        messages.error(request, "This url is broken.")
        return redirect("sign_up")
