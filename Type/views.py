from django.views.generic import ListView
from .models import models
from .models import Type

class TypeView(ListView):
    model = Type
    template_name = 'type_list.html'

