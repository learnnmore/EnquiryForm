from django.urls import path
from . import views

urlpatterns = [
    path('enquiries/', views.enquiry_list, name='enquiry_list'),
    # Other URL patterns...
]
