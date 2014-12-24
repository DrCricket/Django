from django.db import models
from django.utils.encoding import smart_unicode
import math

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    hashval = models.BigIntegerField(blank=True)

    def save(self,*args, **kwargs):
        self.hashval = abs(hash(self.title))
        return super(Entry, self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.title + " " +str(self.hashval))
    
    class Meta:
        verbose_name_plural = 'Entries'