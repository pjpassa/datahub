from django import forms


# Should be a model form
class DatafileUploadForm(forms.Form):
    file = forms.FileField(label="Upload new file")
    has_header_row = forms.BooleanField(label="Use first row as header", required=False)
    name = forms.CharField(max_length=64,
                           required=False,
                           label="Name for uploaded file:",
                           help_text="Leave blank to use file name.")
