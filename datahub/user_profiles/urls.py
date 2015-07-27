from django.conf.urls import include, url
from django.contrib import admin
from user_profiles.views import ProfileDetailView

urlpatterns = [
    url(r'^(?P<pk>d+)/', ProfileDetailView.as_view(), name="public_profile"),
]