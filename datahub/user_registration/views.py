from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
from django.views.generic import FormView, CreateView
from datahub.helpers.mixins import AddContextInAsViewMixin


class LoginView(AddContextInAsViewMixin, FormView):
    form_class = AuthenticationForm
    template_name = "single_form_view.html"

    def get_success_url(self):
        user = User.objects.get(username=self.request.POST["username"])
        try:
            user.profile
        except BaseException:
            return reverse_lazy("profile_creation")
        return reverse_lazy("home")

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super().form_valid(form)


class RegistrationView(AddContextInAsViewMixin, FormView):
    form_class = UserCreationForm
    template_name = "single_form_view.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
