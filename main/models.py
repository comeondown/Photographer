import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from sorl.thumbnail import ImageField, delete
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify
import tempfile
from PIL import Image
from io import BytesIO

class MyFileStorage(FileSystemStorage):

    def save(self, name, content):
        tf = tempfile.NamedTemporaryFile()
        temp_name = os.path.splitext(tf.name)[-1]
        filename, extension = os.path.splitext(name)
        new_name = temp_name + extension
        return super(MyFileStorage, self).save(new_name, content)
    
class MyFileStorageAlbum(MyFileStorage):
	
    def save(self, name, content):
         #FUCK
         return super(MyFileStorage, self).save(name, content)


fs = MyFileStorage(location='/var/www/media/photos/', base_url="/media/photos/")
fs_album =  MyFileStorageAlbum(location='/var/www/media/photos/', base_url="/media/photos/")


class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    theme_image = ImageField(storage=fs_album, default='/img/default.jpg')
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
    	return "{}".format(self.title)

    def admin_thumbnail(self):
        return u'<img src="{0}" width="150px"/>'.format(self.theme_image.url)

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True



class Photo(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    photo = ImageField(storage=fs)
    album = models.ForeignKey('Album')


    def admin_thumbnail(self):
        return u'<img src="{0}" width="200px"/>'.format(self.photo.url)

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


@receiver(pre_delete, sender=Photo)
def mymodel_delete(sender, instance, **kwargs):
    if (instance.photo):
        delete(instance.photo)

class BackgroundImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(storage=fs)
    def admin_thumbnail(self):
        return u'<img src="{0}" width="150px"/>'.format(self.image.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
