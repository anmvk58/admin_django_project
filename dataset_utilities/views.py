from django.shortcuts import render
from django.views import generic


LIST_CONNECTION = [
    {'cnn_name': 'Landing Zone', 'type': 'Oracle', 'host': '10.37.0.116', 'created_by': 'anmv2'},
    {'cnn_name': 'Work Zone', 'type': 'Oracle', 'host': '10.69.0.96', 'created_by': 'anmv2'}
]

LIST_DATASET = [
    {'dataset_name': 'LEAD_MFIRST_Q3', 'cnn_name': 'Landing Zone', 'created_by': 'annmv2', 'status': 'active'},
    {'dataset_name': 'LEAD_CASA_Q3', 'cnn_name': 'Work Zone', 'created_by': 'annmv2', 'status': 'active'}

]

# Create your views here.
class ConnectionManagerView(generic.ListView):
    template_name = "dataset_utilities/conn_manager_index.html"
    context_object_name = "list_connection"

    def get_queryset(self):
        """Return data will inject to view html"""
        return LIST_CONNECTION



class DatasetManagerView(generic.ListView):
    template_name = "dataset_utilities/dataset_manager_index.html"
    context_object_name = "list_dataset"

    def get_queryset(self):
        """Return data will inject to view html"""
        return LIST_DATASET


def create_new_dataset(request):
    return render(request, 'dataset_utilities/create_new_dataset.html')