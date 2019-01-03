import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from sorl.thumbnail import ImageField, delete
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile
import tempfile
from PIL import Image
from io import BytesIO, StringIO
import time

class MyFileStorage(FileSystemStorage):

    def save(self, name, content):
        # Создаем временное имя файла
        #tf = tempfile.NamedTemporaryFile()
        #temp_name = os.path.splitext(tf.name)[-1] 

        timestamp = time.time()
        filename, extension = os.path.splitext(name)
        new_name = str(round(timestamp)) + extension

        return super(MyFileStorage, self).save(new_name, content)

fs = MyFileStorage(location='/var/www/media/photos/', base_url="/media/photos/")

class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    theme_image = models.ImageField(upload_to='photos/', default='/img/default.jpg')
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
    	return "{}".format(self.title)

    def admin_thumbnail(self):
        return u'<img src="{0}" width="150px"/>'.format(self.theme_image.url)
    # compressing image before saving
    def save(self, *args, **kwargs):
        if self.theme_image:
            img = Image.open(BytesIO(self.theme_image.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
        output = BytesIO()
        #if image large then reduce size (width, height)

        if self.theme_image.width > 4000 or self.theme_image.height > 4000:
            img.thumbnail((self.theme_image.width/4, self.theme_image.height/4), Image.ANTIALIAS)
        elif self.theme_image.width > 3000 or self.theme_image.height > 3000:
            img.thumbnail((self.theme_image.width/1.5, self.theme_image.height/3), Image.ANTIALIAS)
        elif self.theme_image.width > 2000 or self.theme_image.height > 2000:
            img.thumbnail((self.theme_image.width/2, self.theme_image.height/2), Image.ANTIALIAS)
        elif self.theme_image.width > 1000 or self.theme_image.height > 1000:
            img.thumbnail((self.theme_image.width/1.5, self.theme_image.height/1.5), Image.ANTIALIAS)
        #reduce quality image to 40%
        img.save(output, format='JPEG', quality=40)
        
        output.seek(0)
        self.theme_image = InMemoryUploadedFile(output, 'ImageField', '{}.jpg'.format(self.theme_image.name.split('.')[0]), 'image/jpg', output.__sizeof__(), None)
        return super(Album, self).save(*args, **kwargs)

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

@receiver(pre_save, sender=Photo)
def mymodel_delete_old_photo(sender, instance, *args, **kwargs):
    oldPhoto = sender.objects.get(id=instance.id)
    if (oldPhoto.photo!=instance.photo):
        fs.delete(oldPhoto.photo)

class BackgroundImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(storage=fs)
    def admin_thumbnail(self):
        return u'<img src="{0}" width="150px"/>'.format(self.image.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
