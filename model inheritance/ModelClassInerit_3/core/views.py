from django.shortcuts import render
from .models import StudentGirls, StudentBoys
# Create your views here.


def home(request):
    studentBoys = StudentBoys.objects.all().order_by('name')
    studentGirls = StudentGirls.objects.all().order_by('id')
    context = {
        'studentBoys': studentBoys,
        'studentGirls': studentGirls
    }
    return render(request, 'core/home.html', context)
