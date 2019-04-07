from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def user_signup(request):
    form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def user_login(request):
    return render(request,'accounts/login.html',{})


