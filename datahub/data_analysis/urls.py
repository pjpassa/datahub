from django.conf.urls import url
from data_analysis.views import DatasetDetailView, ProjectDetailView, ProjectCreateView, ProjectDeleteView, \
    DatasetDeleteView
from fileupload.views import DatafileUploadView

urlpatterns = [
    url(r'^(?P<username>[-_\w]+)/new_project/$', ProjectCreateView.as_view(), name="create_project"),
    url(r'^(?P<username>[-_\w]+)/(?P<project>[-_\w]+)/upload/$',
        DatafileUploadView.as_view(),
        name="upload"),
    url(r'^(?P<username>[-_\w]+)/(?P<project>[-_\w]+)/delete/$',
        ProjectDeleteView.as_view(),
        name="delete_project"),
    url(r'^(?P<username>[-_\w]+)/(?P<project>[-_\w]+)/(?P<dataset>[-_\w]+)/delete/$',
        DatasetDeleteView.as_view(),
        name="dataset_detail"),
    url(r'^(?P<username>[-_\w]+)/(?P<project>[-_\w]+)/(?P<dataset>[-_\w]+)/$',
        DatasetDetailView.as_view(),
        name="dataset_detail"),
    url(r'^(?P<username>[-_\w]+)/(?P<project>[-_\w]+)/$',
        ProjectDetailView.as_view(),
        name="project_detail"),
]
