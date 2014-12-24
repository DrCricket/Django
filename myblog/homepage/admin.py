from django.contrib import admin
from models import Entry
import math

class EntryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
    class Meta:
        model = Entry


admin.site.register(Entry,EntryAdmin)
