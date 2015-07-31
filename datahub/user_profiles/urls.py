from django.conf.urls import url
from user_profiles import views

urlpatterns = [
    url(r'^$', views.ProfileDetailView.as_view(), name="detail"),
]
