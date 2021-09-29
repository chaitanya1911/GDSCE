from django.db import models

# Create your models here.

class Year(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    division = models.CharField(max_length=10)
    studentId= models.IntegerField()
    year= models.ForeignKey(Year,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname
    
