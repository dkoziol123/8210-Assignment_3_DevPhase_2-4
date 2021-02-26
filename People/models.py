from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class People(models.Model):

    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    phone = models.CharField(max_length=50, blank=False, null=True,default=' ')
    email = models.CharField(max_length=50, default=' ')
    #state = models.CharField(max_length=50, default='NE')

    def __str__(self):
        return self.name
