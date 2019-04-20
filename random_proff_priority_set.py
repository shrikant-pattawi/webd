import random, sys, os, django
import math

# sys.path.append("""E:\All_Projects\Python\Django\webd""")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
django.setup()

from accounts.models import User_details
from accounts.models import Team_details
from accounts.models import priority
from django.contrib.auth.models import User


def proff_set():

    mem = User_details.objects.filter(authority=4).filter(data_verified=2)
    mem2 = User_details.objects.filter(authority=5).filter(data_verified=2)

    for i in mem :
        for j in mem2 :
            x = priority()
            x.proff = j.user_user
            x.user_priority = random.randint(1,100)
            x.user = i.user_user
            x.save()

proff_set()