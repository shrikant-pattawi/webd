from django import forms

class signupform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField()
    email=forms.EmailField()
    registration_no=forms.IntegerField()

