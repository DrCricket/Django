from django.contrib import admin

# Register your models here.

from apps.data.models import Entry

admin.site.register(Entry)

