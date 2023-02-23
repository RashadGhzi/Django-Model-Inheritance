from django.db import models

# Create your models here.


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class StudentModel(BaseModel):
    roll = models.IntegerField()
    marks = models.IntegerField()


class TeacherModel(BaseModel):
    salary = models.IntegerField()
