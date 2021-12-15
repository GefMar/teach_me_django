from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

from media_app.models import Media


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    file = models.ForeignKey(Media, on_delete=models.PROTECT, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, related_name="profile")
    phone = models.CharField(
        max_length=16,
        validators=(
            RegexValidator(regex=r"^\+?\d{8,15}$", message="Неверный телефонный номер"),
        ),
        blank=True,
        null=True,
    )
    bio = models.TextField(null=True, blank=True)
    github = models.URLField(max_length=2048, null=True, blank=True)
