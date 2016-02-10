# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('theme_image', models.ImageField(upload_to='/var/www/media/album_covers/', default='/img/default.jpg')),
                ('description', models.CharField(null=True, blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='', storage=main.models.MyFileStorage(base_url='/media/photos/', location='/var/www/media/photos/'))),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('description', models.CharField(null=True, blank=True, max_length=2000)),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to='', storage=main.models.MyFileStorage(base_url='/media/photos/', location='/var/www/media/photos/'))),
                ('album', models.ForeignKey(to='main.Album')),
            ],
        ),
    ]
