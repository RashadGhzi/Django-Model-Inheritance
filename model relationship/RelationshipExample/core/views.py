from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Page, Song, Post
# Create your views here.


class ClassBasedHomeView(View):
    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'core/home.html', context)


class PageView(View):
    def get(self, request):
        # "page" is model class and "page_name" is model field
        users = User.objects.filter(page__page_name='Apple')
        pages = Page.objects.filter(page_name='Apple')
        context = {
            'users': users,
            'pages': pages
        }
        return render(request, 'core/page.html', context)
