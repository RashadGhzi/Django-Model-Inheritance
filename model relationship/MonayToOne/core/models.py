from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # When User object is deleted this post table will not delete
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    post_title = models.CharField(max_length=100)
    post_category = models.CharField(max_length=200)
    post_publish_date = models.DateField()
