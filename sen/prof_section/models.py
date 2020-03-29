from django.db import models

# Create your models here.
class AttendanceRecord(models.Model):
    studentID = models.CharField(max_length=10)
    courseID = models.CharField(max_length=10)
    dateTime = models.DateTimeField()