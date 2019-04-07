from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login,logout

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else :
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Project_Allotment_Portal:home')
