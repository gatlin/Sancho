from django.db import models
from django.contrib import admin
from json_field import JSONField
from django.contrib.auth.models import User
import uuid

class ContentType(models.Model):
    '''
    Represents a content type that the system recognizes.
    These are purely arbitrary but they may hold semantic
    importance for client applications.
    '''
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=10000,default="")

    def __unicode__(self):
        return "%s" % (self.name,)

class ContentTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContentType, ContentTypeAdmin)

class LinkType(models.Model):
    '''
    A unique identifier for types of links among posts.
    Clients may use whatever semantic interpretation they see fit.
    '''
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=10000,default="")

class LinkTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(LinkType, LinkTypeAdmin)

class Post(models.Model):
    '''
    The container for posts.

    Posts are arbitrary JSON wrapped in an object containing various metadata.
    '''
    uid =\
    models.CharField(max_length=256,primary_key=True,default=uuid.uuid4(),blank=True)
    content_type = models.ForeignKey("ContentType",related_name="posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True,auto_now=True)
    content = JSONField()
    owner = models.ForeignKey(User)

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)


class Link(models.Model):
    '''
    A connection between two posts with an associated LinkType
    '''
    from_post = models.ForeignKey(Post,related_name='links')
    to_post   = models.ForeignKey(Post)
    type      = models.ForeignKey(LinkType)

    def __unicode__(self):
        return "/posts/%s/" % (self.to_post.pk,)

class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link,LinkAdmin)
