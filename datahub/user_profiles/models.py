from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
