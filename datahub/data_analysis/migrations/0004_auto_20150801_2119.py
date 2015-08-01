# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0003_auto_20150730_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^[-\\w]+')], max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^[-\\w]+')], max_length=64),
        ),
    ]
