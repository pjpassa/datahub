from django.db import models
from user_profiles.models import Profile
from jsonfield import JSONField


class Project(models.Model):
    profile = models.ForeignKey(Profile)


class Dataset(models.Model):
    project = models.ForeignKey(Project)
    data = JSONField()
