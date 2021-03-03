from django.urls import path
from . import views
from .views import (
    SelectionListView,
    SelectionUpdateView,
    SelectionDetailView,
    SelectionDeleteView,
    SelectionCreateView,

)

urlpatterns = [

    path('<int:pk>/edit2',
         SelectionUpdateView.as_view(), name='selection_edit'),
    path('<int:pk>/detail2/',
         SelectionDetailView.as_view(), name='selection_detail'),
    path('<int:pk>/delete2/',
         SelectionDeleteView.as_view(), name='selection_delete'),
    path('new2/', SelectionCreateView.as_view(), name='selection_new'),
    path('', SelectionListView.as_view(), name='selection_list'),






]
