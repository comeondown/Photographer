# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20151115_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
