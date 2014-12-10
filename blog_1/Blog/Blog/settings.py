"""
Django settings for Blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_DIRS,\
    TEMPLATE_CONTEXT_PROCESSORS, LOGIN_REDIRECT_URL
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!$vllr+3^vhclno40t@)z*-1=!@cs-nt&r6w#))iiin*dtmgx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT= os.path.normpath(os.path.join(BASE_DIR,'static/'))

SITE_ID=1

TEMPLATE_DIRS = (
                 
    #'C:/Users/Utsav/Documents/Workspace/Blog/templates',
    os.path.join(BASE_DIR,'templates'),
                 )



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.flatpages', ## Needed for flatpages
    #'django.contrib.staticfiles',
    'apps.homepage',
    'apps.data',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', ## This is important for sessions
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'Blog.urls'

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'blog.db'), ## Works nicely, that join thing
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS =(
    'django.contrib.auth.context_processors.auth', ## Needed
    'django.core.context_processors.csrf', 
    'django.core.context_processors.media',
    )

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL='/profile/'
LOGIN_URL='/login/'
