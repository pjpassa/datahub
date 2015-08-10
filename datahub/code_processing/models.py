import random
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pandasql import sqldf
from data_analysis.models import Project, Dataset


class SubmittedCode(models.Model):
    code = models.TextField()
    valid = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project)
    results = models.ManyToManyField(Dataset)


@receiver(post_save, sender=SubmittedCode)
def process_code(instance, created, **kwargs):
    if not created:
        return
    project = instance.project
    datasets = {data.name: data.data for data in project.dataset_set.all()}
    code = instance.code
    table_name = None
    if code.startswith("create table"):
        split = code.split(" ")
        table_name = split[2]
        code = " ".join(split[4:])
    if not table_name:
        table_name = "query" + str(random.randint(100000,999999))
    df = sqldf(code, datasets)
    result = Dataset.objects.create(project=project, data=df, name=table_name)
    instance.results.add(result)
    instance.save()
