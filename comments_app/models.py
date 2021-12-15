from django.contrib.auth.models import User
from django.db import models

from publication_app.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="comments")
    text = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name="comments")
