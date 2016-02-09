import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from sorl.thumbnail import ImageField, delete
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify
import tempfile


class MyFileStorage(FileSystemStorage):
    def _save(self, name, content):
        tf = tempfile.NamedTemporaryFile()
        temp_name = os.path.splitext(tf.name)[-1]
        filename, extension = os.path.splitext(name)
        new_name = temp_name + extension
        return super(MyFileStorage, self)._save(new_name, content)

    def save(self, name, content):
        tf = tempfile.NamedTemporaryFile()
        temp_name = os.path.splitext(tf.name)[-1]
        filename, extension = os.path.splitext(name)
        new_name = temp_name + extension
        return super(MyFileStorage, self).save(new_name, content)
    
    
#im not sure this is necessary but afraid to remove
class MyImageField(ImageField):
    def __init__(self, *args, **kwargs):
        super(MyImageField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(MyImageField, self).clean(*args, **kwargs)
        filename = os.path.splitext(data.name)
        data.name = data.name.encode('utf-8').decode('utf-8')
        if len(filename[1]):
            data.name += u'.' + slugify(filename[1])
        return data 

fs = MyFileStorage(location='/var/www/media/photos/', base_url="/media/photos/")


class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    theme_image = ImageField(storage=fs, default='/img/default.jpg')
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
    photo = MyImageField(storage=fs)
    album = models.ForeignKey('Album')


    def admin_thumbnail(self):
        return u'<img src="{0}" width="200px"/>'.format(self.photo.url)

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


@receiver(pre_delete, sender=Photo)
def mymodel_delete(sender, instance, **kwargs):
    if (instance.photo):
        delete(instance.photo)
