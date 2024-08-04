from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class GeneralInfo(models.Model):
    agency_name = models.CharField(max_length=255, default="Agency")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.agency_name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Blog(models.Model):
    image = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    content = RichTextField()

    def __str__(self):
        return self.title
