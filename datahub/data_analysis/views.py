from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from data_analysis.models import Dataset, Project
from datahub.helpers.mixins import ProvideProfileMixin, AddProfileToFormMixin
from fileupload.forms import DatafileUploadForm


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(DetailView):
    model = Dataset
    template_name = "data_analysis/dataset_head.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username", None)
        project_name = self.kwargs.get("project", None)
        dataset_name = self.kwargs.get("dataset", None)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': User._meta.verbose_name})
        try:
            project = Project.objects.get(profile=user.profile, name=project_name)
        except Project.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Project._meta.verbose_name})
        try:
            dataset = Dataset.objects.get(project=project, name=dataset_name)
        except Dataset.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Dataset._meta.verbose_name})
        return dataset


class DatasetDeleteView(DeleteView):
    model = Dataset


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = "data_analysis/project_detail.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username", None)
        project_name = self.kwargs.get("project", None)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': User._meta.verbose_name})
        try:
            project = Project.objects.get(profile=user.profile, name=project_name)
        except Project.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Project._meta.verbose_name})
        return project

    def get_context_data(self, **kwargs):
        context = {"upload_form": DatafileUploadForm}
        context.update(kwargs)
        return super().get_context_data(**context)


class ProjectDeleteView(DeleteView):
    model = Project


class ProjectCreateView(AddProfileToFormMixin, CreateView):
    model = Project
    template_name = 'create_view.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("user_profile", kwargs={"username": self.request.user.username})