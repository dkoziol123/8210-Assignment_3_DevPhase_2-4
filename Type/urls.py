from django.urls import path
from . import views
from .views import (
    TypeListView,
    TypeUpdateView,
    TypeDetailView,
    TypeDeleteView,
    TypeCreateView,

)

urlpatterns = [
    path('<int:pk>/edit3',
         TypeUpdateView.as_view(), name='type_edit'),
    path('<int:pk>/detail3/',
         TypeDetailView.as_view(), name='Type_detail'),
    path('<int:pk>/delete3/',
         TypeDeleteView.as_view(), name='type_delete'),
    path('new3/', TypeCreateView.as_view(), name='type_new'),
    path('', TypeListView.as_view(), name='type_list'),

]
