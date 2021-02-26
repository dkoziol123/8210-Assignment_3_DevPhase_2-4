from django.urls import path
from . import views

urlpatterns = [

    path('', views.TypeView.as_view(), name='type_list'),

]
