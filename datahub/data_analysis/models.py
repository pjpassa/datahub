from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from picklefield import PickledObjectField
from datahub.helpers.validators import start_with_letter_validator, contains_only_letters_dash_underscore_validator
from user_profiles.models import Profile


class Project(models.Model):
    name = models.CharField(max_length=64,
                            validators=[start_with_letter_validator,
                                        contains_only_letters_dash_underscore_validator])
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
    name = models.CharField(max_length=128,
                            validators=[start_with_letter_validator,
                                        contains_only_letters_dash_underscore_validator])
    project = models.ForeignKey(Project)
    data = PickledObjectField()
    head = PickledObjectField()
    column_list = PickledObjectField()
    num_obs = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("name", "project")

    def __str__(self):
        return "{}/{}/{}".format(self.project.profile.user.username,
                                 self.project.name,
                                 self.name)

    def as_html(self, head=True):
        if head:
            return self.head.to_html()
        return self.data.tail.to_html()

    @property
    def head_as_html(self):
        return self.as_html()

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

    @property
    def api_link(self):
        return reverse_lazy("api:dataset",
                            kwargs={"pk": self.pk})

@receiver(pre_save, sender=Dataset)
def update_head(instance, **kwargs):
    if instance.data is not None:
        instance.head = instance.data.head(20)
        instance.column_list =instance.head.columns
        instance.num_obs = len(instance.data.index)
