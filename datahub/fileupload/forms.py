from django import forms


class DatafileUploadForm(forms.Form):
    file = forms.FileField(label="Upload new file")
    has_header_row = forms.BooleanField(label="Does your file have headers?", required=False)


