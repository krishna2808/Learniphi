from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .admin import UserCreationForm
from user.forms import UserLogin
from django.contrib.auth import authenticate, login, logout 
from user.models import User 
from django.urls import reverse



# Create your views here.


def account(request):
     signin_form  = UserLogin()
     signup_form  = UserCreationForm() 
     if request.method == 'POST':

          if request.POST.get('name'):
               signup_form  = UserCreationForm(request.POST)
               if signup_form.is_valid():
                    name = signup_form.cleaned_data.get('name')
                    email = signup_form.cleaned_data.get('email')
                    password = signup_form.cleaned_data.get('password')
                    User.objects.create_user(email=email, name=name, password=password).save() 
                    return  HttpResponseRedirect(reverse('dashboard'))
                    
          else: 
               signin_form  = UserLogin(request.POST)
               if signin_form.is_valid():
                    email = signin_form.cleaned_data.get('email')
                    password = signin_form.cleaned_data.get('password')
                    user = authenticate(request, email=email , password=password)
                    if user is not None: 
                       return  HttpResponseRedirect(reverse('dashboard'))
                    #   return HttpResponseRedirect('/dashboard') 
                       
     context = {'title' : 'Account Opening',
                'signin_form' : signin_form,
                'signup_form' : signup_form
               }                 
     return render(request, 'user/account.html', context=context)
