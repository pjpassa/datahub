import json
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from data_analysis.models import Dataset, Project
from fileupload.forms import DatafileUploadForm
import pandas as pd


class DatafileuploadView(FormView):
    template_name = 'fileupload/datafile_upload.html'
    form_class = DatafileUploadForm
    success_url = reverse_lazy("profile:list")

    def form_valid(self, form):
        df = pd.read_csv(self.get_form_kwargs().get('files')['file'])
        project = Project(profile=self.request.user.profile)
        project.save()
        dataset = Dataset(data=json.loads(df.to_json()), project=project)
        dataset.save()
        # self.id = dataset.id
        return super().form_valid(form)
