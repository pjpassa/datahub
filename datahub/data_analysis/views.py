from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from pandasql import sqldf
from data_analysis.forms import CodeForm
from data_analysis.models import Dataset, Project
from datahub.helpers.mixins import AddProfileToFormMixin, VerifyUserBeforeDeletionMixin, ProvideProjectFromURLMixin, \
    ProvideDatasetFromURLMixin, AddContextInAsViewMixin
from fileupload.forms import DatafileUploadForm


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(ProvideDatasetFromURLMixin, DetailView):
    model = Dataset
    template_name = "data_analysis/dataset.html"

    def get_context_data(self, **kwargs):
        context = {"code_form": CodeForm}
        context.update(kwargs)
        return super().get_context_data(**context)


class DatasetDeleteView(ProvideDatasetFromURLMixin, VerifyUserBeforeDeletionMixin, DeleteView):
    model = Dataset

    def get_success_url(self):
        return reverse_lazy("data_analysis:project_detail",
                            kwargs={"username": self.kwargs.get("username"),
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


class ProjectCreateView(AddContextInAsViewMixin, AddProfileToFormMixin, CreateView):
    model = Project
    template_name = 'single_form_view.html'
    fields = ['name']
    additional_context = {"panel_title": "Create Project",
                          "submit_button_name": "Create"}

    def get_success_url(self):
        return reverse_lazy("data_analysis:project_detail",
                            kwargs={"username": self.request.user.username,
                                    "project": self.get_form_kwargs().get("data").get("name")})


class DatasetQueryView(ProvideDatasetFromURLMixin, UpdateView):
    template_name = 'data_analysis/dataset_query.html'

    def get_context_data(self, **kwargs):
        context = {"code_form": CodeForm}
        context.update(kwargs)
        return super().get_context_data(**context)

    def post(self, request, *args, **kwargs):
        pass


def dataset_query_view(request, username, project, dataset):
    if request.POST:
        user = User.objects.get(username=username)
        project = Project.objects.get(name=project, profile=user.profile)
        dataset = Dataset.objects.get(name=dataset, project=project)
        datasets = {data.name: data.data for data in project.dataset_set.all()}
        code = request.POST.get("code")
        context = {'result': sqldf(code, datasets).head(20).to_html(),
                   object: dataset,
                   code: code}
        return render_to_response("data_analysis/dataset_query.html", context=context)
