from django.urls import path,re_path
from django.urls import include
from . import views

app_name= 'Project_Allotment_Portal'

urlpatterns = [

     re_path(r'^$', views.home, name="home"),

     #path('',views.signup, name='signup'),

     #re_path(r'^/profile', views.profile, name="profile"),

     #path('details/',views.details, name="details"),
     #path('adduser',views.add_user,name="adduser")
]
