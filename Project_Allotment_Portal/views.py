from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'base.html',{})

def home(request):
    return render(request,'home2.html',{})