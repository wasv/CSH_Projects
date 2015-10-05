# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pms.models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0002_auto_20151003_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.ImageField(upload_to=pms.models.get_project_path, blank=True),
        ),
    ]
