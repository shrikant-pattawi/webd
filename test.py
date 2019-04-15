import random, sys, os, django
import math

#sys.path.append("""E:\All_Projects\Python\Django\webd""")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Project.settings")
django.setup()

from accounts.models import User_details
from django.contrib.auth.models import User



def populate(n) :
    for i in range(0,n) :
        us = User.objects.create_user("test_user_"+str(i), password='pass12@0')
        us.save()

        us_det = User_details()
        us_det.user_user = us
        us_det.user_reg_no = 20164000+i
        us_det.user_email = "user_" + str(i) + "@mnnit.ac.in"
        us_det.user_name = "user" + str(i)
        us_det.user_gender = 'M'
        us_det.user_cpi = random.randint(1,1000)/100.0
        us_det.user_bio = "hi bye"
        us_det.contact = 1000000000+i
        us_det.authority = 0
        us_det.data_verified =1
        us_det.save()

def verifyall() :

    mem = User_details.objects.filter(data_verified=1)

    for i in mem:
        i.data_verified=2
        i.save()


def groups() :

    n = len(User_details.objects.filter(data_verified=2))
    a = math.ceil(n/4)

    for i in range (1,5):
        temp = User_details.objects.filter(data_verified=2).order_by('user_cpi')[(i-1)*a:i*a]
        for j in temp :
            j.authority = i
            j.save()


#populate(40)
verifyall()
groups()