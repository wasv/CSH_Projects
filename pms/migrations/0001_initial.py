# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('bio', models.TextField()),
                ('website', models.URLField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('last_update', models.DateField(verbose_name=datetime.datetime(2015, 9, 21, 2, 6, 2, 639442, tzinfo=utc))),
                ('state', models.CharField(choices=[('C', 'Concept'), ('O', 'Ongoing'), ('D', 'Done'), ('A', 'Abandoned')], max_length=1)),
                ('website', models.URLField()),
                ('documentation', models.URLField()),
                ('contributors', models.ManyToManyField(related_name='pms_project_contributors', to='pms.Profile')),
                ('owner', models.ForeignKey(related_name='pms_project_owner', to='pms.Profile')),
            ],
        ),
    ]
