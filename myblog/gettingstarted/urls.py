from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^entry/(?P<entrynumber>\d+)/','homepage.views.blog',name='blog'),
    url(r'^about/','homepage.views.about',name='about'),
    url(r'^home/','homepage.views.home',name='home'),
    url(r'^search/(?P<search_term>\w+)/','homepage.views.search',name='search'),
    url(r'^archive/','homepage.views.archive',name='archive'),
    url(r'^', 'homepage.views.home', name='homeredirect'), ## Default URL 
)
