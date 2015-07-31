from django.core.urlresolvers import reverse_lazy
from django.db import models
from picklefield import PickledObjectField
from user_profiles.models import Profile


class Project(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile)

    class Meta:
        unique_together = ("name", "profile")

    def __str__(self):
        return "{}/{}".format(self.profile.user.username, self.name)

    @property
    def link(self):
        return reverse_lazy("data_analysis:project_detail",
                            kwargs={"username": self.profile.user.username,
                                    "project": self.name})

    def dataset_upload_link(self):
        return reverse_lazy("data_analysis:upload",
                            kwargs={"username": self.profile.user.username,
                                    "project": self.name})


class Dataset(models.Model):
    name = models.CharField(max_length=64)
    project = models.ForeignKey(Project)
    data = PickledObjectField()

    class Meta:
        unique_together = ("name", "project")

    def __str__(self):
        return "{}/{}/{}".format(self.project.profile.user.username,
                                 self.project.name,
                                 self.name)

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

    @property
    def query_link(self):
        return reverse_lazy("data_analysis:dataset_query",
                            kwargs={"username": self.project.profile.user.username,
                                    "project": self.project.name,
                                    "dataset": self.name})

    @property
    def link(self):
        return reverse_lazy("data_analysis:dataset_detail",
                            kwargs={"username": self.project.profile.user.username,
                                    "project": self.project.name,
                                    "dataset": self.name})
