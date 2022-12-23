from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
#from store.models import TaggedItemManager

# Create your models here.
class Tag(models.Model):
  label = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.label


class TagItem(models.Model):
  #objecs = TaggedItemManager()
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  content_type= models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey()
