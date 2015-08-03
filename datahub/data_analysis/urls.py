from django.conf.urls import url
from data_analysis.api import DatasetRetrieveAPIView
from data_analysis.views import DatasetDetailView, ProjectDetailView, ProjectCreateView, ProjectDeleteView, \
    DatasetDeleteView, DatasetQueryView, dataset_query_view
from fileupload.views import DatafileUploadView

urlpatterns = [
    url(r'^(?P<username>[-\w]+)/new_project/$', ProjectCreateView.as_view(), name="create_project"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/upload/$',
        DatafileUploadView.as_view(),
        name="upload"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/delete/$',
        ProjectDeleteView.as_view(),
        name="delete_project"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/(?P<dataset>[-\w]+)/delete/$',
        DatasetDeleteView.as_view(),
        name="dataset_detail"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/(?P<dataset>[-\w]+)/api/$',
        DatasetRetrieveAPIView.as_view(),
        name="temp_api"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/(?P<dataset>[-\w]+)/$',
        DatasetDetailView.as_view(),
        name="dataset_detail"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/$',
        ProjectDetailView.as_view(),
        name="project_detail"),

    url(r'^(?P<username>[-\w]+)/(?P<project>[-\w]+)/(?P<dataset>[-\w]+)/query/$',
        dataset_query_view,
        name="dataset_query"),

]
