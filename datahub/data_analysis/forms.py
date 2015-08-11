from django import forms
from data_analysis.models import Project


class ProjectForkForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name"]
