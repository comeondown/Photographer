# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment_admin_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='showed',
            new_name='hide',
        ),
    ]
