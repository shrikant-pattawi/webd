from django.contrib import admin
from . import models

admin.site.register(models.User_details)
admin.site.register(models.Team_details)
admin.site.register(models.user_requests)

# Register your models here.
