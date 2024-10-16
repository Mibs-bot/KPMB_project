from django.db import models

# Create your models here.
class Programme(models.Model):
    programmecode = models.CharField(max_length = 8, primary_key=True)
    programmename = models.TextField(max_length = 50)
    programmeaccdate = models.DateField(null=True)
    programmeduration = models.IntegerField(default = 3)

class mentor(models.Model):
    mentorcode = models.CharField(max_length = 8, primary_key=True)
    mentorname = models.TextField(max_length = 50)
    mentoraccdate = models.DateField(null=True)

class Student(models.Model):
    studentid = models.CharField(max_length = 10, primary_key = True)
    studentname = models.TextField(max_length=225)
    studentemail = models.CharField(max_length = 225)
    studentage = models.PositiveSmallIntegerField(default = 0)
    studentmentor = models.ForeignKey('mentor',on_delete=models.CASCADE)
    