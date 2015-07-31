from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from datahub.helpers.mixins import ProvideProfileMixin, AddUserToFormMixin, LoginRequiredMixin
from user_profiles.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'user_profiles/public_profile.html'

    def get_object(self, queryset=None):
        return User.objects.get(username=self.kwargs.get("username")).profile


class ProfileListView(ListView):
    model = Profile
    template_name = 'user_profiles/profile_list.html'


class ProfileUpdateView(ProvideProfileMixin, UpdateView):
    model = Profile
    template_name = 'user_profiles/profile_update.html'
    success_url = reverse_lazy("profile:update")
    fields = ['name', 'email']


class ProfileCreateView(LoginRequiredMixin, AddUserToFormMixin, CreateView):
    model = Profile
    template_name = 'create_view.html'
    success_url = reverse_lazy("profile:update")
    fields = ['name', 'email']
