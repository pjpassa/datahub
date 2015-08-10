# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0002_auto_20150807_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittedCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('valid', models.BooleanField(default=False)),
                ('processed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(to='data_analysis.Project')),
                ('results', models.ManyToManyField(to='data_analysis.Dataset')),
            ],
        ),
    ]
