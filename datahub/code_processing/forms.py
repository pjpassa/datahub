from django import forms
from code_processing.models import SubmittedCode


class CodeForm(forms.ModelForm):
    code = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SubmittedCode
        fields = ['code']