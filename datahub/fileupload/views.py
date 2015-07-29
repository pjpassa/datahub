from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from fileupload.forms import DatafileUploadForm
from fileupload.uploadhandler import handle_datafile_upload


class DatafileUploadView(FormView):
    template_name = 'fileupload/datafile_upload.html'
    form_class = DatafileUploadForm
    success_url = reverse_lazy("profile:list")

    def form_valid(self, form):
        print("I am here")
        handle_datafile_upload(self.get_form_kwargs().get('files')['file'],
                               self.get_form_kwargs().get('data'),
                               self.request.user)
        return super().form_valid(form)
