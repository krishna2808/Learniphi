

from django.urls import path
from .views import account



urlpatterns = [
    path('',  account, name= "sign_in"),
    # path('dashboard/',  dashboard, name= "dashboard"),
]