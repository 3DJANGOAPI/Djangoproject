from django.db import models

# Create your models here.
class Student(models.model):
    name=models.CharField(max_length=30)
    marks=mudels.IntegerField()
