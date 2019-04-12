from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from . import forms
from .models import User_details
from django.core.exceptions import ObjectDoesNotExist

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
            try:
                temp = User_details.objects.get(user_user=user)
                request.session['gamer_data_verified'] = temp.data_verified
                request.session['gamer_authority'] = temp.authority
            except ObjectDoesNotExist:
                pass
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else :
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Project_Allotment_Portal:home')

def user_profile(request):
    update(request)
    if request.method == 'POST':
        form = forms.ProfileDetails(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_user = request.user
            temp.data_verified = 1
            temp.save()
            return redirect('Project_Allotment_Portal:home')
    else:
        form = forms.ProfileDetails()

        # try:
        #     form = forms.ProfileDetails()
        #     temp_ = User_details.objects.get(user_user=request.user)
        #     verification_status = temp_.data_verified
        # except ObjectDoesNotExist:
        #     form = forms.ProfileDetails()
        #     verification_status = 0

        # if 'gamer' in request.session:
        #     return render(request, 'accounts/test.html')
        #     #form = forms.ProfileDetails(instance=User_details.objects.get(user_reg_no=request.session['gamer']));
        # else:
        #     form = forms.ProfileDetails()
    return render(request, 'accounts/profile.html', {'form':form} )


def user_team(request):
    update(request)
    return render(request, 'accounts/team.html')


def update(request):
    try:
        temp = User_details.objects.get(user_user=request.user)
        request.session['gamer_data_verified'] = temp.data_verified
        request.session['gamer_authority'] = temp.authority
    except ObjectDoesNotExist:
        request.session['gamer_data_verified'] = 0
        request.session['gamer_authority'] = 0


