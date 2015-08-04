from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from datahub.helpers.mixins import ProvideProfileMixin, AddUserToFormMixin, LoginRequiredMixin, AddContextInAsViewMixin
from user_profiles.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'user_profiles/public_profile.html'

    def get_object(self, queryset=None):
        return User.objects.get(username=self.kwargs.get("username")).profile


class ProfileListView(ListView):
    model = Profile
    template_name = 'user_profiles/profile_list.html'


class ProfileUpdateView(AddContextInAsViewMixin, ProvideProfileMixin, UpdateView):
    additional_context = {"panel_title": "Update Profile", "submit_button_name": "Update"}
    model = Profile
    template_name = 'single_form_view.html'
    fields = ['name', 'email']

    def get_success_url(self):
        return reverse_lazy("user_profile", kwargs={"username": self.request.user.username})


class ProfileCreateView(AddContextInAsViewMixin, LoginRequiredMixin, AddUserToFormMixin, CreateView):
    additional_context = {"panel_title": "Create Profile", "submit_button_name": "Create"}
    model = Profile
    template_name = 'single_form_view.html'
    fields = ['name', 'email']

    def get_success_url(self):
        return reverse_lazy("user_profile", kwargs={"username": self.request.user.username})
