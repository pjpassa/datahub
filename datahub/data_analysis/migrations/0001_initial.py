# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('data', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('profile', models.ForeignKey(to='user_profiles.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='project',
            field=models.ForeignKey(to='data_analysis.Project'),
        ),
    ]
