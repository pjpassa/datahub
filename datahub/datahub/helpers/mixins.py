from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from data_analysis.models import Project, Dataset
from datahub.helpers.decorators import provide_profile, require_profile


class ProvideProfileMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return provide_profile(view)


class ProfileRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return require_profile(view)


class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)


class AddUserToFormMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class AddProfileToFormMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.profile = self.request.user.profile
        return super().form_valid(form)


class VerifyUserBeforeDeletionMixin:

    def delete(self, request, *args, **kwargs):
        if self.kwargs.get("username") != request.user.username:
            return HttpResponseRedirect(reverse_lazy("home"))
        return super().delete(request, *args, **kwargs)


class ProvideDatasetFromURLMixin:

    def get_object(self, queryset=None):
        username = self.kwargs.get("username", None)
        project_name = self.kwargs.get("project", None)
        dataset_name = self.kwargs.get("dataset", None)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print("User does not exist")
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': User._meta.verbose_name})
        try:
            project = Project.objects.get(profile=user.profile, name=project_name)
        except Project.DoesNotExist:
            print("Project does not exist")
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Project._meta.verbose_name})
        try:
            dataset = Dataset.objects.get(project=project, name=dataset_name)
        except Dataset.DoesNotExist:
            print("Dataset does not exist")
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Dataset._meta.verbose_name})
        return dataset


class ProvideProjectFromURLMixin:

    def get_object(self, queryset=None):
        username = self.kwargs.get("username", None)
        project_name = self.kwargs.get("project", None)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print("User does not exist")
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': User._meta.verbose_name})
        try:
            project = Project.objects.get(profile=user.profile, name=project_name)
        except Project.DoesNotExist:
            print("Project does not exist")
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Project._meta.verbose_name})
        return project
