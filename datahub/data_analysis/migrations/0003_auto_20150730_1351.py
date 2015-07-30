# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0002_auto_20150730_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
