from django.urls import path
from . import views

urlpatterns = [
    path('conn-manager/', views.ConnectionManagerView.as_view(), name='connection_manager'),
    path('dataset-manager/', views.DatasetManagerView.as_view(), name='dataset_manager'),
]