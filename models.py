from django.db import models

# Create your models here.
class Student(models.Model):
    versity_id = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    cgpa = models.FloatField()

class Teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length=20)


class Course(models.Model):
    Title = models.CharField(max_length=20)
    Code = models.CharField(max_length=20)
    Credit = models.IntegerField()


