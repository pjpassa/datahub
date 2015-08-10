# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(message='Name must start with a letter or _.', regex='^[A-Za-z_]'), django.core.validators.RegexValidator(message='Name must contain only alphanumeric                                                                  characters or the _ character.', regex='^[-\\w]*$')])),
                ('data', picklefield.fields.PickledObjectField(editable=False)),
                ('head', picklefield.fields.PickledObjectField(editable=False)),
                ('columns', picklefield.fields.PickledObjectField(editable=False)),
                ('num_obs', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(message='Name must start with a letter or _.', regex='^[A-Za-z_]'), django.core.validators.RegexValidator(message='Name must contain only alphanumeric                                                                  characters or the _ character.', regex='^[-\\w]*$')])),
                ('profile', models.ForeignKey(to='user_profiles.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='project',
            field=models.ForeignKey(to='data_analysis.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'profile')]),
        ),
        migrations.AlterUniqueTogether(
            name='dataset',
            unique_together=set([('name', 'project')]),
        ),
    ]
