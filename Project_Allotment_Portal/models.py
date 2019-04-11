from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Team_details(models.Model):

    # team_id= models.IntegerField(verbose_name="team_id",default=1)
    # team_leader_name=models.CharField(verbose_name="team_leader",max_length=100,default=1)

    team_name = models.CharField(verbose_name="team_name",max_length=100)
    team_leader = models.ForeignKey(User, related_name="leader", default=None, on_delete=models.CASCADE)
    team_member_2 = models.ForeignKey(User, default=None, related_name="member2", on_delete=models.SET_NULL, null=True)
    team_member_3 = models.ForeignKey(User, default=None, related_name="member3", on_delete=models.SET_NULL, null=True)
    team_member_4 = models.ForeignKey(User, default=None, related_name="member4", on_delete=models.SET_NULL, null=True)
    team_cpi = models.DecimalField(verbose_name="cpi", max_digits=4 , decimal_places=2,blank=False)


    def __str__(self):
        return self.team_name

class Notification(models.Model):

    # notification_id=models.IntegerField(verbose_name="not_id" ,default=1)

    notification_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE, verbose_name="user_type", null=True)
    notification_content=models.CharField(verbose_name="content", max_length=500 )

    def __str__(self):
        return self.notification_type

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
#
