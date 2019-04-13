import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project.settings')
import django
django.setup()

from accounts.models import User_details

def populate() :
    for i in range(1,5) :

        User_details.user_reg_no=i
        if i%2==0 :
            User_details.user_gender='M'
        else :
            User_details.user_gender = 'F'
        User_details.user_contact=i*100000000
        User_details.user_cpi=i%8
        User_details.user_email="user"+str(i)+"@gmail.com"
        User_details.user_name="user"+(i)
        User_details.data_verified=1
        User_details.authority=2
        User_details.save()

populate()