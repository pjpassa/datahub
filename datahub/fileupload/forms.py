from django.forms import forms


class DatafileUploadForm(forms.Form):
    file = forms.FileField(label="Upload new file")


