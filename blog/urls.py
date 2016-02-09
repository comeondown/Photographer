from django.conf.urls import url
from django.contrib import admin
import blog.views as views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	url(r'^$', views.index_blog,name='index_blog'),
    url(r'^([0-9])$', views.PostListView.as_view(),name='blog'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post'),
]

