# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_processing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedcode',
            name='results',
            field=models.ManyToManyField(null=True, to='data_analysis.Dataset'),
        ),
    ]
