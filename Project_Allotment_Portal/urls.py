from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    #path('',views.signup, name='signup'),


     path('details/',views.details, name="details"),
     path('adduser',views.add_user,name="adduser")
]
