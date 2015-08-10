# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='columns',
            new_name='column_list',
        ),
    ]
