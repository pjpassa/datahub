from django.conf.urls import url, include
from data_analysis.views import DatasetDetailView, ProjectDetailView, ProjectCreateView
from fileupload.views import DatafileUploadView
from user_profiles import urls as profile_urls
from user_profiles.views import ProfileDetailView

urlpatterns = [
    url(r'^new_project/', ProjectCreateView.as_view(), name="create_project"),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/upload/$',
        DatafileUploadView.as_view(),
        name="upload"),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<dataset>\w+)/$',
        DatasetDetailView.as_view(),
        name="dataset_detail"),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/$',
        ProjectDetailView.as_view(),
        name="project_detail"),
]
