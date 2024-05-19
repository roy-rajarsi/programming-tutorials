from .models import Student

from django.contrib import admin
from typing import List


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display: List[str] = ['id', 'name']
