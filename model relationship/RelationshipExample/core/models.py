from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, primary_key=True)
    page_name = models.CharField(max_length=200)
    page_category = models.CharField(max_length=200)
    page_publish_date = models.DateField()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200)
    post_catergory = models.CharField(max_length=200)
    post_publish_date = models.DateField()


class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=200)
    song_duration = models.DecimalField(max_digits=3, decimal_places=2)
