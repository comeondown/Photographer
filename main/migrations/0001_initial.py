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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('theme_image', sorl.thumbnail.fields.ImageField(storage=main.models.MyFileStorageAlbum(location='/var/www/media/photos/', base_url='/media/photos/'), default='/img/default.jpg', upload_to='')),
                ('description', models.CharField(blank=True, null=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(storage=main.models.MyFileStorage(location='/var/www/media/photos/', base_url='/media/photos/'), upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, null=True, max_length=2000)),
                ('photo', sorl.thumbnail.fields.ImageField(storage=main.models.MyFileStorage(location='/var/www/media/photos/', base_url='/media/photos/'), upload_to='')),
                ('album', models.ForeignKey(to='main.Album')),
            ],
        ),
    ]
