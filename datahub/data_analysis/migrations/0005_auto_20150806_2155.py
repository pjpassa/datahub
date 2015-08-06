# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0004_auto_20150801_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='head',
            field=picklefield.fields.PickledObjectField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Name must start with a letter or _.', regex='^[A-Za-z_]'), django.core.validators.RegexValidator(message='Name must contain only alphanumeric                                                                  characters or the _ character.', regex='^[-\\w]*$')], max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Name must start with a letter or _.', regex='^[A-Za-z_]'), django.core.validators.RegexValidator(message='Name must contain only alphanumeric                                                                  characters or the _ character.', regex='^[-\\w]*$')], max_length=64),
        ),
    ]
