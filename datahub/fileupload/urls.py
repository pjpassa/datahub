from django.conf.urls import url
from fileupload import views

urlpatterns = [
    url(r'upload/', views.DatafileuploadView.as_view(), name="datafile"),
]
