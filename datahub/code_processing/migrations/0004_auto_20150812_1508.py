# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0002_auto_20150807_1913'),
        ('code_processing', '0003_auto_20150810_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submittedcode',
            name='results',
        ),
        migrations.AddField(
            model_name='submittedcode',
            name='result',
            field=models.OneToOneField(null=True, to='data_analysis.Dataset'),
        ),
    ]
