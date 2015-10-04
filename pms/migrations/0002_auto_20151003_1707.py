# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pms.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=pms.models.get_profile_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(blank=True, related_name='pms_project_contributors', to='pms.Profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='documentation',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, related_name='pms_project_owner', to='pms.Profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
