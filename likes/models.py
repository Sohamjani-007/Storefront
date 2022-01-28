from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class like(models.Model):
    label = models.CharField(max_length=255)


class LikedItem(models.Model):
    # what tag applied to what object
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Type (products, video,article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

