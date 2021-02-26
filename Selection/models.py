from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Selection(models.Model):

    Preference = models.CharField(max_length=50,blank=False, null=False, default=' ')
    Budget_Dollar = models.PositiveIntegerField( blank=False, null=True,default=' 5')
    Time_Frame_Hour = models.PositiveIntegerField( default=' 5')
    #state = models.CharField(max_length=50, default='NE')

    def __str__(self):
        return self.Preference

    #Preference = models.CharField(max_length=50)
    #Budget_Dollar = models.IntegerField(max_length=6)
    #0Time_Frame_Hour = models.IntegerField(max_length=2)