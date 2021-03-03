from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Selection(models.Model):

    Preference = models.CharField(max_length=50,blank=False, null=False, default=' ')
    Budget_Dollar = models.PositiveIntegerField( blank=False, null=True,default=' 5')
    Time_Frame_Hour = models.PositiveIntegerField( default=' 5')
    #state = models.CharField(max_length=50, default='NE')
    author = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.Preference


    def get_absolute_url(self):
        return reverse('selection_detail', args=[str(self.id)])
