# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151108_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='theme_image',
            field=sorl.thumbnail.fields.ImageField(default='/img/default.jpg', upload_to='', storage=main.models.MyFileStorage(base_url='/media/photos/', location='/var/www/media/photos/')),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=main.models.MyImageField(upload_to='', storage=main.models.MyFileStorage(base_url='/media/photos/', location='/var/www/media/photos/')),
        ),
    ]
