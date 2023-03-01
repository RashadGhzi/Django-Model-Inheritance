from django.contrib import admin
from .models import StudentBoys, StudentGirls
# Register your models here.


@admin.register(StudentBoys)
class StudentBoysAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cgpa', 'gender']


@admin.register(StudentGirls)
class StudentGirlsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cgpa', 'gender']
