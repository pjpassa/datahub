import pandas as pd
from data_analysis.models import Project, Dataset


def handle_datafile_upload(file, form, user, project=None):
    if not project:
        project = Project(profile=user.profile)
        project.save()
    if form.get("has_header_row"):
        df = pd.read_csv(file)
    else:
        df = pd.read_csv(file, header=None)
    name = form.get("name") or str(file).split(".")[0]
    dataset = Dataset(data=df, project=project, name=name)
    dataset.save()
