from django.conf.urls import url
from data_analysis.api import DatasetRetrieveAPIView

urlpatterns = [
    url(r'^dataset/(?P<pk>\d+)/$', DatasetRetrieveAPIView.as_view(), name="dataset")
]