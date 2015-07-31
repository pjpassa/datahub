from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

urlpatterns = [
    url(r'', CreateView.as_view(form_class=UserCreationForm,
                                template_name='registration/registration.html',
                                success_url='home',)),
]