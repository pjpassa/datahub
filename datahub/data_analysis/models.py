import collections
from django.db import models
import pandas as pd
from picklefield import PickledObjectField
from user_profiles.models import Profile
from jsonfield import JSONField


class Project(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile)

    class Meta:
        unique_together = ("name", "profile")


class Dataset(models.Model):
    name = models.CharField(max_length=64)
    project = models.ForeignKey(Project)
    data = PickledObjectField()

    class Meta:
        unique_together = ("name", "project")

    def as_html(self, num_rows=0, head=None):
        df = self.data
        if num_rows:
            if head is None:
                raise ValueError("num_rows was defined, but head was not set. Define head as True or False")
            if head:
                df = df.head(num_rows)
            else:
                df = df.tail(num_rows)
        return df.to_html()

    @property
    def head_as_html(self):
        return self.as_html(20, True)
