from rest_framework import generics
from data_analysis.models import Dataset
from data_analysis.serializers import DatasetSerializer


class DatasetRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DatasetSerializer


    def get_queryset(self):
        return Dataset.objects.all()
