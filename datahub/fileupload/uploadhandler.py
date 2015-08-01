import random
import re
from django.core.exceptions import ValidationError
import pandas as pd
from data_analysis.models import Project, Dataset
from datahub.helpers.validators import start_with_letter_validator


def handle_datafile_upload(file, form, user, project=None):
    if not project:
        project = Project(profile=user.profile, name="_{}".format(random.randint(10000,99999)))
        project.save()
    name = form.get("name") or str(file).split(".")[0]
    dataset = Dataset(data=None, project=project, name=name)
    if form.get("has_header_row"):
        df = pd.read_csv(file, encoding="utf-8")
    else:
        df = pd.read_csv(file, header=None, encoding="utf-8")
    columns = [re.sub(r'[^-\w]', "_", str(column)) for column in df.columns]
    for index, value in enumerate(columns):
        try:
            print("here")
            start_with_letter_validator(value)
        except ValidationError:
            print("I am here")
            columns[index] = "_" + value
        columns[index] = value[:128]
    df.columns = columns
    dataset.data = df
    dataset.save()
