from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, video, article)
    # ID
    ContentType = models.ForeignKey(ContentType, on_delete=models.CASCADE) # allowing Generic relationship
    objects_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()