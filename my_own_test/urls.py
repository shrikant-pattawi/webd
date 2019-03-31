from django.urls import path
from . import views

urlpatterns = [
    path('',views.first, name='first'),
    path('sec',views.first, name='first'),
]
