import random, sys, os, django
import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Project.settings")
django.setup()

from accounts.models import User_details
from accounts.models import Team_details


mem = User_details.objects.filter(data_verified=1)

for i in mem:
    i.data_verified=2
    i.save()

    # separate in groups

n = len(User_details.objects.filter(data_verified=2).filter(authority__lte = 4))
a = math.ceil(n/4)

for i in range (1,5):
    temp = User_details.objects.filter(data_verified=2).filter(authority__lte = 4).order_by('-user_cpi')[(i-1)*a:i*a]
    for j in temp :
        j.authority = 5-i
        j.save()

temp = User_details.objects.filter(data_verified=2).filter(authority__lte = 4).order_by('-user_cpi')[(0) * a:1 * a]
for j in temp:
    x = Team_details()
    x.team_cpi = j.user_cpi
    x.team_leader = j.user_user
    x.team_name = j.user_name
    x.save()

