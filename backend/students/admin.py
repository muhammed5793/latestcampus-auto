
# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_number', 'name', 'department', 'email')
    search_fields = ('admission_number', 'name')
