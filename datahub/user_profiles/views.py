from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from user_profiles.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'user_profiles/public_profile.html'
