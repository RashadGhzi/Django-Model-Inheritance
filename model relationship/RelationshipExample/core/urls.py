from django.urls import path
from core.views import *

urlpatterns = [
    path('', ClassBasedHomeView.as_view(), name='home'),
    path('page/', PageView.as_view(), name='page')
]
