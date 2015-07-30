from django.db import models
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
    data = JSONField()

    class Meta:
        unique_together = ("name", "project")
