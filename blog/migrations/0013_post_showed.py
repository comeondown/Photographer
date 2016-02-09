# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151216_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='showed',
            field=models.BooleanField(default=True),
        ),
    ]
