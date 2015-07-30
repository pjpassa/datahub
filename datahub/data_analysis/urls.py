from django.conf.urls import url
from data_analysis.views import DatasetDetailView, ProjectDetailView
from fileupload.views import DatafileUploadView


urlpatterns = [
    url(r'^(?P<username>\w+)/(?P<project>\w+)/upload',
        DatafileUploadView.as_view(),
        name="upload"),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<dataset>\w+)$',
        DatasetDetailView.as_view(),
        name="dataset_detail"),
    url(r'^(?P<username>\w+)/(?P<project>\w+)$',
        ProjectDetailView.as_view(),
        name="project_detail"),
]
