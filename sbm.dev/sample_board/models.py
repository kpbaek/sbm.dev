from django.db import models
from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class DjangoBoard(models.Model):
      subject = models.CharField(max_length=50, blank=True)
      name = models.CharField(max_length=50, blank=True)
      created_date = models.DateField(null=True, blank=True)
      mail = models.CharField(max_length=50, blank=True)
      memo = models.CharField(max_length=200, blank=True)
      hits = models.IntegerField(null=True, blank=True)



class Entry(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)