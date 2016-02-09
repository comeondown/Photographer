# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20151219_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
