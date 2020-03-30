from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AttendanceRecord(models.Model):
    studentID = models.CharField(max_length=10)
    courseID = models.CharField(max_length=10)
    dateTime = models.DateTimeField()


class Prof(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    courses = models.CharField(max_length=100)
    