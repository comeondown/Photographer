from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView
from main.models import Album, Photo
from Photographer import settings



def index(request):
	print([ x.title for x in Album.objects.all()])
	return render_to_response("index.html", context = {'body_class':"body-index"});

def doesntworking(request):
	return render_to_response("doesntworking.html");


def portfolio(request):
	albums = Album.objects.all()
	return render_to_response("portfolio.html", context={'albums':albums, 'body_class':"body-photo"})


def contacts(request):
	return render_to_response("contacts.html", context={'body_class':"body-contacts"})

def about(request):
	return render_to_response("about.html", context={'body_class':"body-about"})


class PhotoList(ListView):

	template_name = 'photo_list.html'

	def get_queryset(self):
		self.album = Album.objects.get(title=self.args[0])
		return self.album.photo_set.all()

	def get_context_data(self, **kwargs):
		context = super(PhotoList, self).get_context_data(**kwargs)
		context['album'] = self.album
		context['body_class'] = 'body-photo'
		return context

