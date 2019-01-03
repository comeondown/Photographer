from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView
from main.models import Album, Photo, BackgroundImage
from Photographer import settings

# List of albums will pass to templates
# via main.context_processors.global_albums_context_processor

def index(request):
	back = BackgroundImage.objects.filter(title="main")[0]
	background_url = back.image.url
	return render(
		request,
		"index.html", 
		{'body_class':"body-index", "background_url":background_url}
	)

def doesntworking(request):
	return render_to_response("doesntworking.html");


def portfolio(request):
	return render(
		request,
		"portfolio.html", 
		{'body_class':"body-photo"}
	)


def contacts(request):
	back = BackgroundImage.objects.filter(title="contacts")[0]
	background_url = back.image.url
	return render(
		request,
		"contacts.html", 
		{'body_class':"body-background", 'background_url':background_url}
	)

def about(request):
	back = BackgroundImage.objects.filter(title="about")[0]
	background_url = back.image.url
	return render(
		request,
		"about.html", 
		{'body_class':"body-about", 'background_url':background_url,}
	)


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

