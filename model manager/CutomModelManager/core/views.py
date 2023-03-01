from django.shortcuts import render
from .models import StudentModel
# Create your views here.


def home(request):
    studentInfo = StudentModel.objects.all()
    studentManagerInfo = StudentModel.students.all()
    # it will query that objects where there all have cgpa greater then 3.0 and less then 4.0
    studentCGPARange = StudentModel.studentCGPA.cgpa_range(3.00, 4.00)
    # it will query objects that all object have marks = 400
    studentMarks = StudentModel.student_marks.marks_manager(400)
    context = {
        'studentInfo': studentInfo,
        'studentManagerInfo': studentManagerInfo,
        'studentCGPARange': studentCGPARange,
        'studentMarks': studentMarks,
    }
    return render(request, 'core/home.html', context)
