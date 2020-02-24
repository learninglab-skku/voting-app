
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

from courses.models import Group, Section, Course



class Grade(models.Model):

    student = models.ForeignKey("accounts.student", on_delete=models.CASCADE) # Lazy Reference for being created automatically when student is generated. 
    middle_score = models.IntegerField(null=True, blank=True)

    final_score = models.IntegerField(null=True, blank=True)

    attendance_score = models.IntegerField(null=True, blank=True)

    total_web_work_score = models.IntegerField(null=True, blank=True)

    total_pre_class_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.student.name + ' ' + str(self.student.student_no)


class AttendanceInstance(models.Model):

    # Lazy Reference for being created automatically when student is generated. 
    student = models.ForeignKey("accounts.student", on_delete=models.CASCADE)

    status = models.BooleanField(default = False)

    datestamp = models.DateField(default=datetime.date.today)
    
    def __str__(self):

        return self.student.name + ' ' + str(self.student.student_no) + ' ' +str(self.datestamp)



