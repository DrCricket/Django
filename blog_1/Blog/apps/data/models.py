from django.core.signals import request_finished
from django.db.models.signals import post_save


from django.db import models
from apps.data.managers import EntryManager
from apps.data import handlers


class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title   = models.CharField(max_length=50)
    text    = models.TextField()
    published = models.BooleanField(db_index=True,default=True)
    objects = EntryManager() ## Relate to entry manager
    
    def __unicode__(self):
        return u"%s %s"%(self.created,self.title)
    
    class Meta:
        verbose_name_plural = 'Entries'

post_save.connect(handlers.model_saved) ## Need to understand this better
request_finished.connect(handlers.request_finished) ## This too