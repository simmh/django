from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.


# class Article(models.Model):
#     STATUS_CHOICES = Choices('draft', 'published')
#     # ...
#     status = StatusField(choices_name='STATUS_CHOICES')


class Category(models.Model):
    name = models.CharField(max_length=80)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.id, self.name)


class Post(models.Model):
    STATUS_CHOICES = Choices('draft', 'published')
    status = StatusField(choices_name='STATUS_CHOICES')
    category = models.ForeignKey(
        Category, blank=True, null=True,  on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tag = TaggableManager(blank=True)

    def __str__(self):
        return "%s %s - %s - %s" % (self.id, self.category, self.title, self.body)


# reply model 3
# -body
# -created
# -updated
