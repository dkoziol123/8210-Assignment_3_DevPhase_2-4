from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Selection
from django.urls import reverse_lazy


class SelectionListView(ListView):
    model = Selection
    template_name = 'selections/selection_list.html'

class SelectionDetailView(DetailView):
    model = Selection
    template_name = 'selections/selection_detail.html'
    login_url = 'login'

class SelectionUpdateView(UpdateView):
    model = Selection
    fields = ('Preference', 'Budget_Dollar', 'Time_Frame_Hour',)
    template_name = 'selections/selection_edit.html'

class SelectionDeleteView(DeleteView):
    model = Selection
    template_name = 'selections/selection_delete.html'
    success_url = reverse_lazy('selection_list')

class SelectionCreateView(CreateView):
    model = Selection
    template_name = 'selections/selection_new.html'
    fields = ('Preference', 'Budget_Dollar', 'Time_Frame_Hour', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
