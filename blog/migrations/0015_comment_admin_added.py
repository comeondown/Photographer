# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_showed'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='admin_added',
            field=models.BooleanField(default=False),
        ),
    ]
