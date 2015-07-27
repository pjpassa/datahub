from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

urlpatterns = [
    url(r'', CreateView.as_view(form_class=UserCreationForm,
                                template_name='user_registration/registration.html',
                                success_url='home',)),
]