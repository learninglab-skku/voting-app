
from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Group, Section, Course



class Grade(models.Model):
   #student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, related_name='Grade.student+', unique=True)
   student = models.ForeignKey("accounts.student", on_delete=models.CASCADE) # Lazy Reference for being created automatically when student is generated. 
   middle_score = models.IntegerField(null=True, blank=True)
   
   final_score = models.IntegerField(null=True, blank=True)
   
   attendance_score = models.IntegerField(null=True, blank=True)
   
   total_web_work_score = models.IntegerField(null=True, blank=True)
   
   total_pre_class_score = models.IntegerField(null=True, blank=True)

   



