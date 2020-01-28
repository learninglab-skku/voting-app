from django.db import models

from courses.models import Course
from django.urls import reverse


class Video(models.Model):
    video_name = models.CharField(max_length = 500, null = False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.video_name} ({self.course.title}, {self.course.year})"

    def get_absolute_url(self):
        return reverse('onlineclasses:detail', kwargs={'pk': self.pk, })