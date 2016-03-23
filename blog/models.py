from django.db import models
from django.db.models import Model

# for django cms
from cms.models import CMSPlugin

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    body = models.TextField()
    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField('date published')

class BlogPluginModel(CMSPlugin):
    blog = models.ForeignKey('blog.Post', related_name='plugins')

    def __unicode__(self):
      return self.blog.id
