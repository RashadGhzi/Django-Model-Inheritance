from django.contrib import admin
from .models import StudentModel, TeacherModel
# Register your models here.


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'roll', 'marks']


@admin.register(TeacherModel)
class TeacherModel(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'salary', 'date']
