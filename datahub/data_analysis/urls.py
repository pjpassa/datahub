from django.conf.urls import url
from data_analysis.views import DatasetDetailView, ProjectDetailView

urlpatterns = [
    url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<dataset>\w+)$',
        DatasetDetailView.as_view(),
        name="dataset_detail"),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<dataset>\w+)$',
        ProjectDetailView.as_view(),
        name="project_detail"),
]