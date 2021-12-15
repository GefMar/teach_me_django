from django.db import models

from publication_app.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')
