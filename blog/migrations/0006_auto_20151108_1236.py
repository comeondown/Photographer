# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151107_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=tinymce.models.HTMLField(max_length=1000),
        ),
    ]
