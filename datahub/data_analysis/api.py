from rest_framework import generics
from data_analysis.models import Dataset, Project
from data_analysis.serializers import DatasetSerializer, ProjectSerializer


class DatasetRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DatasetSerializer


    def get_queryset(self):
        return Dataset.objects.all()


class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
