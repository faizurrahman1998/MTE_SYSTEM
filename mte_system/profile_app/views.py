from django.shortcuts import render, redirect
from django.contrib import messages
from auth_app.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

#helper_function
from mte_system.Helper import Helper_Functions


@login_required(login_url="sign_in")
def profile_dash(request): 

    context = {
        "title": "Dashboard"
    }
    return render(request, "profile_app/profile.html", context)


def update_profile(request): 
    
    context = {
            "title": "Update Profile"
        }

    if request.user.is_authenticated: 

        if request.method == "POST": 
            
            form = UserChangeForm(request.POST, request.FILES, instance=request.user)

            if form.is_valid():

                Helper_Functions.delete_image(request)
                form.save()

                messages.success(request, "Profile Updated")
                
                return redirect("dash")

            else: 
                context.update({"form" : form})
                return render(request, "profile_app/update.html", context)



        return render(request, "profile_app/update.html", context)
    
    else: 
        return redirect("sign_in")

