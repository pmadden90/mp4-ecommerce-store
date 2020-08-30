from django.db import models # noqa
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True) # noqa

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    tab_title = models.CharField(max_length=255, default="About Shannon Gaels")
    header_image = models.ImageField(null=True, blank=True, upload_to="media/club_images/") # noqa    
    body = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # noqa

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about', args=(str(self.id)))
