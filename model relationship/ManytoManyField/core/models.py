from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=200)
    song_duration = models.DecimalField(max_digits=3, decimal_places=2)

    def written_by(self):
        return f"{[str(name) for name in self.user.all()]}"
