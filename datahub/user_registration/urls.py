from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from user_registration.views import RegistrationView

urlpatterns = [
    url(r'', RegistrationView.as_view(additional_context={"panel_title": "Registration", "submit_button_name": "Register"}),
        name="register"),
    url(r'k', CreateView),
]
