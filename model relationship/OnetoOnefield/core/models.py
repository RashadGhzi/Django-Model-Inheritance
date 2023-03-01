from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
    # When user delete this page model also delete
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    # user = models.OneToOneField(
    #     User, on_delete=models.PROTECT, primary_key=True)  # First page delete after user can delete

    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})  # is_stuff= True user can create this model table
    page_name = models.CharField(max_length=100)
    page_category = models.CharField(max_length=100)
    page_publish_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.page_name} page user is {self.user}"
