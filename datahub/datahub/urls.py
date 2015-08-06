"""datahub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy
from user_profiles.views import ProfileListView, ProfileCreateView, ProfileUpdateView, ProfileDetailView
from user_registration import urls as user_reg
from data_analysis import urls as data_analysis
from api import urls as api_url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^register/', include(user_reg, namespace="register")),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': reverse_lazy("home")}),
    url(r'^accounts/login/$', login, name="login"),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', ProfileListView.as_view(), name="home"),
    url(r'^new_profile/$', ProfileCreateView.as_view(), name="profile_creation"),
    url(r'^update_profile/$', ProfileUpdateView.as_view(), name="update"),
    url(r'^(?P<username>[-_\w]+)/$', ProfileDetailView.as_view(), name="user_profile"),
    url(r'^', include(data_analysis, namespace="data_analysis")),
    url(r'^api/$', include(api_url, namespace="api")),
]
