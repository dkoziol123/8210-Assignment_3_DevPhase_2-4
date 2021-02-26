from django.urls import path
from . import views

urlpatterns = [

    path('', views.SelectionView.as_view(), name='selection_list'),

]
