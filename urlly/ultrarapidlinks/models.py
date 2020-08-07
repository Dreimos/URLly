from django.db import models
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.conf import settings

from model_utils.models import TimeStampedModel

class StoredURL(TimeStampedModel):
    url = models.URLField("Real URL", unique=True)
    slug = models.SlugField("Internal slug", unique=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        slug_save(self, 5)
        super(StoredURL, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("ultrarapidlinks:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.url)

def slug_save(obj, length):
    if not obj.slug:
        obj.slug = get_random_string(length)
        slug_invalid = True
        while slug_invalid:
            slug_invalid = False
            same_type_objects = type(obj).objects.filter(slug=obj.slug)
            if len(same_type_objects) > 0:
                slug_invalid = True
            if slug_invalid:
               obj.slug = get_random_string(length)