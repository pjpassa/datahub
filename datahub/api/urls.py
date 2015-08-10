from django.conf.urls import url
from code_processing.api import SubmittedCodeCreateAPIView
from data_analysis.api import DatasetRetrieveAPIView

urlpatterns = [
    url(r'^dataset/(?P<pk>\d+)/$', DatasetRetrieveAPIView.as_view(), name="dataset"),
    url(r'^submittedcode/$', SubmittedCodeCreateAPIView.as_view(), name="code"),
]