"""mte_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from auth_app import views as auth_app_views
from profile_app import views as profile_app_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_app_views.sign_in, name='sign_in'),
    path("signup/", auth_app_views.sign_up, name='sign_up'),
    path("logout/", auth_app_views.log_out, name="log_out"),
    path("verification/<uid64>/<token>", auth_app_views.verification, name="verification"),
    path("<username>/change-password/", auth_app_views.change_password, name="change_password"),

    path("<username>/", profile_app_views.profile_dash, name='dash'),
    path("<username>/update/", profile_app_views.update_profile, name="update_profile"), 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
