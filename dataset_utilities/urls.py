from django.urls import path
from . import views

urlpatterns = [
    path('conn-manager/', views.ConnectionManagerView.as_view(), name='connection_manager'),
    path('dataset-manager/', views.DatasetManagerView.as_view(), name='dataset_manager'),
    path('create-dataset/', views.create_new_dataset, name='create_dataset'),
]