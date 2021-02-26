from django.views.generic import ListView
from .models import models
from .models import Selection

class SelectionView(ListView):
    model = Selection
    template_name = 'selection_list.html'
