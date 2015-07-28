from django.conf.urls import url
from user_profiles import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/', views.ProfileDetailView.as_view(), name="detail"),
    url(r'^new/$', views.ProfileCreateView.as_view(), name="creation"),
    url(r'^list/$', views.ProfileListView.as_view(), name="list"),
    url(r'^update/$', views.ProfileUpdateView.as_view(), name="update"),
]
