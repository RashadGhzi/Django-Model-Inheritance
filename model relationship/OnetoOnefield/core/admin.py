from django.contrib import admin
from core.models import Page
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name',
                    'page_category', 'page_publish_date', 'user']
