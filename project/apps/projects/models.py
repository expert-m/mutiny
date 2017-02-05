from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='project_members')
    tech_stack = TaggableManager()
    is_closed = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_project'
