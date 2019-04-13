from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


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
