"""
URL configuration for student_enquiry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from enquiries import views
# from register import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('register/registration_success/', views.registration_success, name='registration_success'),
    # Add this for the success page
    path('admin/', admin.site.urls),
    path('enquiries/', views.enquiry_list, name='enquiry_list'),

    path('enquiry/', views.enquiry_view, name='enquiry'),
    path('enquiry/success/', views.enquiry_success_view, name='enquiry_success'),
    path('', views.home, name='home'),  # Home page

    path('trainer/', views.trainer_view, name='trainer'),
    path('trainer/success/', views.trainer_success_view, name='trainer_success'),
    path('trainer_list/', views.trainer_list, name='trainer_list'),

    path("accounts/", include("django.contrib.auth.urls")),  # new
    #path("", TemplateView.as_view(template_name="home.html"), name="home"),

    #Generate Receipt
    # path(r'generateReceipt/<str:search_string>/', views.generate_receipt, name='generate_receipt'),
    path('generateReceipt/', views.generate_receipt, name='generateReceipt'),
    path('testReceipt/', views.testReceipt, name='testReceipt'),
    path('reGenerateReceipt/', views.reGenerateReceipt, name='reGenerateReceipt'),


    path('', lambda request: redirect('login')),  # Redirects root to 'login'
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Default login view
]
