from django.contrib import admin
from details.models import Student
from details.models import Teacher
from details.models import Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)

