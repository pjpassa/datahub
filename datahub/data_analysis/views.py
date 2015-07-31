from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from data_analysis.models import Dataset, Project
from datahub.helpers.mixins import AddProfileToFormMixin, VerifyUserBeforeDeletionMixin, ProvideProjectFromURLMixin, \
    ProvideDatasetFromURLMixin
from fileupload.forms import DatafileUploadForm


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(ProvideDatasetFromURLMixin, DetailView):
    model = Dataset
    template_name = "data_analysis/dataset_head.html"


class DatasetDeleteView(ProvideDatasetFromURLMixin, VerifyUserBeforeDeletionMixin, DeleteView):
    model = Dataset

    def get_success_url(self):
        return reverse_lazy("data_analysis:project", kwargs={"username": self.kwargs.get("username"),
                                               "project": self.kwargs.get("project")})


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(ProvideProjectFromURLMixin, DetailView):
    model = Project
    template_name = "data_analysis/project_detail.html"

    def get_context_data(self, **kwargs):
        context = {"upload_form": DatafileUploadForm}
        context.update(kwargs)
        return super().get_context_data(**context)


class ProjectDeleteView(ProvideProjectFromURLMixin, VerifyUserBeforeDeletionMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("")

    def get_success_url(self):
        return reverse_lazy("user_profile", kwargs={"username": self.request.user.username})


class ProjectCreateView(AddProfileToFormMixin, CreateView):
    model = Project
    template_name = 'create_view.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("data_analysis:user_profile", kwargs={"username": self.request.user.username})
