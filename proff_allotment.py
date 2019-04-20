import random, sys, os, django
import math

#sys.path.append("""E:\All_Projects\Python\Django\webd""")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Project.settings")
django.setup()

from accounts.models import User_details
from accounts.models import Team_details
from accounts.models import priority
from django.contrib.auth.models import User



def allot() :

    team = Team_details.objects.all().order_by('-team_cpi')

    for i in team :
        a = i.team_leader
        x = priority.objects.filter(user=i.team_leader).order_by('user_priority')
        for j in x :
            i.professor = j.proff
            i.save()
            priority.objects.filter(proff=i.professor).delete()
            priority.objects.filter(user=i.team_leader).delete()
            break
        i.data_verified = 5
        i.save()

allot()