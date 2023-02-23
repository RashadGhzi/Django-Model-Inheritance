from django.db import models

# Create your models here.


class StudentBoys(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)


class StudentGirls(StudentBoys):
    class Meta:
        proxy = True
