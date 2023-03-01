from django.db import models
from django.db.models import Q
from decimal import Decimal


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all().order_by('name')


class StudentCGPAManager(models.Manager):
    def cgpa_range(self, cgpa1, cgpa2):
        return super().get_queryset().filter(Q(cgpa__gte=cgpa1) & Q(cgpa__lte=cgpa2))


class MarksManager(models.Manager):
    def marks_manager(self, marks_num):
        return super().get_queryset().filter(marks=marks_num)
