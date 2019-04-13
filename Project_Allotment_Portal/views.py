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

# def update(request):
#     try:
#         if request.user.is_authenticated:
#             temp = User_details.objects.get(user_user=request.user)
#             request.session['gamer_data_verified'] = temp.data_verified
#             request.session['gamer_authority'] = temp.authority
#         else :
#             request.session['gamer_data_verified'] = 0
#             request.session['gamer_authority'] = 0
#     except ObjectDoesNotExist:
#         request.session['gamer_data_verified'] = 0
#         request.session['gamer_authority'] = 0
