from django.conf.urls import url
from fileupload import views

urlpatterns = [
    url(r'upload/', views.DatafileUploadView.as_view(), name="datafile"),
]
