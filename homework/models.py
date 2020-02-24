from django.db import models
from courses.models import Course
from accounts.models import Student


class Homework(models.Model):
    title = models.CharField(max_length=255)

    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    
    due_date = models.CharField(max_length=255, null=True)

    optional_readings = models.CharField(max_length=255, null=True, blank=True)
    video_clip_name_1 = models.CharField(max_length=255, null=True, blank=True)
    video_clip_link_1 = models.CharField(max_length=255, null=True, blank=True)
    video_clip_name_2 = models.CharField(max_length=255, null=True, blank=True)
    video_clip_link_2 = models.CharField(max_length=255, null=True, blank=True)
    video_clip_name_3 = models.CharField(max_length=255, null=True, blank=True)
    video_clip_link_3 = models.CharField(max_length=255, null=True, blank=True)
    
    # quetions_image = models.ImageField(upload_to="homework/", null=True)
    questions = models.TextField(blank=True)
    
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = (('title', 'Course'),)

    def __str__(self):
        return f"(Homework {self.title})"

        


class HomeworkTraker(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    Homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=True)

    start_time = models.DateTimeField(null=True)
    start_time_video_1 = models.DateTimeField(null=True)
    start_time_video_2 = models.DateTimeField(null=True)
    start_time_video_3 = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    class Meta:
        unique_together =(('Student', 'Homework'),)
