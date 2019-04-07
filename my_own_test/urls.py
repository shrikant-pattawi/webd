from django.urls import path
from . import views

app_name = 'test'

urlpatterns = [
    path('',views.first, name='first'),
    path('sec',views.first, name='first'),
]
