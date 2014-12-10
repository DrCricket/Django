from django.conf.urls import patterns, include, url
from django.contrib import admin
from Blog import settings 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('apps.homepage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^static/(?P<path>.*)$', 'django.views.static.serve' , {'document_root':settings.MEDIA_ROOT})
)
