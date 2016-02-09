# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_album_theme_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='theme_image',
            field=sorl.thumbnail.fields.ImageField(default='/img/default.jpg', storage=django.core.files.storage.FileSystemStorage(base_url='/media/photos/', location='media/photos/'), upload_to=''),
        ),
    ]
