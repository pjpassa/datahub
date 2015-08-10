# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_processing', '0002_auto_20150810_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedcode',
            name='results',
            field=models.ManyToManyField(to='data_analysis.Dataset'),
        ),
    ]
