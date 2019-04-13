from django.urls import path,re_path
from django.urls import include
from . import views

app_name = 'Project_Allotment_Portal'

urlpatterns = [

     path('',views.home, name='home'),
     re_path(r'^contact/$', views.contact, name='contact'),
     re_path(r'^notification/$', views.notification, name='notification'),

     # re_path(r'^$', views.home, name="home"),
     # re_path(r'^/profile', views.profile, name="profile"),
     # path('details/',views.details, name="details"),
     # path('adduser',views.add_user,name="adduser")
]
