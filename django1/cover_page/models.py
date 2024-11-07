from django.db import models

# Create your models here.

class Student(models.Model):
    university_name = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    dept = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
