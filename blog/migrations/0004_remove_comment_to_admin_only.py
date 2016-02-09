# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151104_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='to_admin_only',
        ),
    ]
