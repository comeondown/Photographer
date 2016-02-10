from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView, FormView

from .models import Post, Comment
from main.models import BackgroundImage
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse

def index_blog(request):
	return HttpResponseRedirect('1')
#Django has paginate_by parameter in ListView that belong to MultipleObjectMixin
#If i will add comments on post page, i would need use this feature
class PostListView(ListView):
	template_name = 'index_blog.html'

	def get_queryset(self):
		posts_list = Post.objects.all().order_by('-date_created')
		paginator = Paginator(posts_list, 10)

		page = self.args[0]
		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)
		return posts

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		back = BackgroundImage.objects.filter(title='blog')[0]
		background_url = back.image.url
		context['body_class'] = 'body-background'
		context['background_url'] = background_url
		return context


class PostDetailView(DetailView):

	model = Post
	slug = 'id'
	template_name = 'post.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		back = BackgroundImage.objects.filter(title='blog')[0]
		background_url = back.image.url
		context['form'] = CommentForm()
		context['comms'] = self.get_object().comment_set.all();
		context['body_class'] = 'body-background'
		context['background_url'] = background_url
		print(context['comms'])
		return context


class PostCommentAdd(SingleObjectMixin, FormView):
	template_name = 'post.html'
	form_class = CommentForm
	model = Post

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super(PostCommentAdd, self).post(self, request, *args, **kwargs)

	def form_valid(self, form):
		user = self.request.user
		if user.is_superuser:
			form.author = 'Ludmila L'
		form.save(self.object, user)
		return HttpResponseRedirect(reverse('post', args=[self.object.id]))

	def get_context_data(self, **kwargs):
		context = super(PostCommentAdd, self).get_context_data(**kwargs)
		context['comms'] = self.get_object().comment_set.all();
		print(context['comms'])
		return context


class PostDetail(View):

	def get(self, request, *args, **kwargs):
		view = PostDetailView.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = PostCommentAdd.as_view()
		return view(request, *args, **kwargs)
