# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20151219_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='showed',
            new_name='hide',
        ),
    ]
