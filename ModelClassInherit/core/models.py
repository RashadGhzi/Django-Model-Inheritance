from django.db import models

# Create your models here.


class BaseModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        abstract = True


class StudentModel(BaseModel):
    roll = models.IntegerField()
    marks = models.FloatField()


class TeacherModel(BaseModel):
    salary = models.CharField(max_length=100)
    date = models.DateField()
