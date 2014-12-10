from django.conf.urls import  *
## THIS IS WRONG - from django.contrib.auth import login,logout
from django.contrib.auth.views import login,logout


urlpatterns = patterns('apps.homepage.views',
    url(r'^$','index',name='homepage_index'),
    url(r'^about/$','about',name='homepage_about'),
    url(r'^contact/$','contact',name='homepage_contact'),
    url(r'^archive/$','archive',name='homepage_archive'),
    url(r'^profile/$','archive',name='homepage_profile'),
                       )


urlpatterns+=patterns('',
    url(r'login/$',login,kwargs={'template_name':'homepage/login.html'},name='homepage_login'),
    url(r'logout/$',logout,kwargs={'next_page':'/'},name='homepage_logout'),
              )