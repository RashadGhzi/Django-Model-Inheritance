from django.contrib import admin
from .models import BaseModel, StudentModel, TeacherModel
# Register your models here.


@admin.register(BaseModel)
class BaseModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'roll', 'marks']


@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'salary']
