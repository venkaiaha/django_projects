from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    marks=models.CharField(max_length=3)

    def __str__(self):
        return self.sname

class Subject(models.Model):
    subject=models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    def __str__(self):
        return self.faculty