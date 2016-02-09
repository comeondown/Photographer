# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151101_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
