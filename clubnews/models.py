from django.db import models # noqa
from django.contrib.auth.models import User
import datetime


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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # noqa

    def __str__(self):
        return self.title + '|' + str(self.author)
