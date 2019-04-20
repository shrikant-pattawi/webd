import random, sys, os, django
import math

#sys.path.append("""E:\All_Projects\Python\Django\webd""")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Project.settings")
django.setup()

from accounts.models import User_details
from accounts.models import Team_details
from django.contrib.auth.models import User



def allot() :



    for i in range(0,n) :
        us = User.objects.create_user("test_proff_"+str(i), password='pass12@0')
        us.save()

        us_det = User_details()
        us_det.user_user = us
        us_det.user_reg_no = 20464000+i
        us_det.user_email = "prof_user_" + str(i) + "@mnnit.ac.in"
        us_det.user_name = "proff" + str(i)
        us_det.user_gender = 'M'
        us_det.user_cpi = random.randint(1,1000)/100.0
        us_det.user_bio = "hi bye"
        us_det.contact = 100000000+i
        us_det.authority = 5
        us_det.data_verified =2
        us_det.save()

allot()