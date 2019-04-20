import random, sys, os, django
import math

#sys.path.append("""E:\All_Projects\Python\Django\webd""")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Project.settings")
django.setup()

from accounts.models import User_details
from accounts.models import Team_details
from django.contrib.auth.models import User

def team_form() :

    mem1 = User_details.objects.filter(authority=1).filter(data_verified=2)
    mem2 = User_details.objects.filter(authority=2).filter(data_verified=2)
    mem3 = User_details.objects.filter(authority=3).filter(data_verified=2)
    mem4 = User_details.objects.filter(authority=4).filter(data_verified=2)
    tm = Team_details.objects.all()
    a=len(mem1)
    b=len(mem2)
    c=len(mem3)
    d=len(mem4)

    for i in tm:
        try :
            x = User_details.objects.filter(authority=1).filter(data_verified=2).first()
            i.team_member_1 = x.user_user
            x.data_verified = 3
            x.save()
        except :
            pass

        try :
            x = User_details.objects.filter(authority=2).filter(data_verified=2).first()
            i.team_member_1 = x.user_user
            x.data_verified = 3
            x.save()
        except :
            pass

        try :
            x = User_details.objects.filter(authority=3).filter(data_verified=2).first()
            i.team_member_1 = x.user_user
            x.data_verified = 3
            x.save()
        except :
            pass
        i.save()

team_form()