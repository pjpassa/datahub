# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=64, default='temp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, default='temp'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='dataset',
            unique_together=set([('name', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'profile')]),
        ),
    ]
