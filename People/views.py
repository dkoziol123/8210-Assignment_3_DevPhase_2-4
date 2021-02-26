from django.views.generic import ListView
from .models import models
from .models import People

class PeopleView(ListView):
    model = People
    template_name = 'people_list.html'
