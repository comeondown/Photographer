from django.conf.urls import url, include
from django.contrib import admin
import main.views as views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings


urlpatterns = [
    url(r'^admpan108/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^portfolio/([\w|\W]+)', views.PhotoList.as_view(), name="photo_list"),
    url(r'^portfolio/$', views.portfolio, name="portfolio"),
    url(r'^contacts/$', views.contacts, name="contacts"),
    url(r'^about/$', views.about, name="about"),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.doesntworking, name='index'),
    url(r'^redactor/', include('redactor.urls')),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()

