from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from accounts.views import update
# Create your views here.

def first(request):
    return render(request,'base.html',{})

def home(request):
    update(request)
    return render(request,'home2.html',{})

def contact(request):
    update(request)
    return render(request,'contact.html',{})

def notification(request):
    update(request)
    return render(request,'notification.html',{})

