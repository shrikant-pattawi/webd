from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from accounts.views import update
# Create your views here.
from Project_Allotment_Portal.mail import send_mail
def first(request):
    return render(request,'base.html',{})

def home(request):
    update(request)
    return render(request,'home2.html',{})

def contact(request):
    update(request)
    if request.method =='POST' :
        try :
            data = request.POST.copy()
            send_mail(data.get('email'), data.get('subject'), data.get('comment'))
            return render(request,'contact_success.html',{})
        except Exception as e:
            return render(request, 'contact_failure.html', {'e':e})

    return render(request,'contact.html',{})

def notification(request):
    update(request)
    return render(request,'notification.html',{})

