# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Album, Photo, BackgroundImage

class PhotosInline(admin.StackedInline):
	model = Photo
	extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    def photosAll(self, obj):
    	html = ''
    	images = obj.photo_set.all()
    	for i in images:
    		if i.name:
    			html = html + "Фото:" + i.name + "<br/>"
    		else:
    			html = html + "Фото:#БезНазвания# <br/>"
    	return html

    photosAll.allow_tags = True

    readonly_fields = ['photosAll']
    fields = ['title', 'theme_image', 'photosAll']
    list_display = ('title','admin_thumbnail',)
    inlines = [PhotosInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	fields = ['name', 'photo', 'description', 'album' ]
	list_display = ('id','name', 'admin_thumbnail', 'description', 'album')



@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    fields = ['title', 'image']
    list_display = ('title', 'admin_thumbnail')
