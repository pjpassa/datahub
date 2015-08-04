from rest_framework import generics
from data_analysis.models import Dataset
from data_analysis.serializers import DatasetSerializer
from datahub.helpers.mixins import ProvideDatasetFromURLMixin


class DatasetRetrieveAPIView(ProvideDatasetFromURLMixin, generics.RetrieveAPIView):
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()
