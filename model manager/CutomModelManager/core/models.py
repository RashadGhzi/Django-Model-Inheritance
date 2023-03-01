from django.db import models
from .managers import StudentManager, StudentCGPAManager, MarksManager
# Create your models here.


class StudentModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    marks = models.IntegerField()
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)

    objects = models.Manager()
    students = StudentManager()
    studentCGPA = StudentCGPAManager()
    student_marks = MarksManager()

    def __str__(self) -> str:
        return self.name
