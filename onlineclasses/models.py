from django.db import models

from courses.models import Course, Lecture, Group
from django.urls import reverse
from accounts.models import Student
from votes.models import Question


class Video(models.Model):
    video_name = models.CharField(max_length = 255, null = True, blank = True)
    video_link = models.CharField(max_length = 255, null = True, blank = True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.video_name} ({self.lecture}, {self.course})"

    def get_absolute_url(self):
        return reverse('onlineclasses:detail', kwargs={'pk': self.pk, })


class VideoTracker(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)

    first_vote_submit = models.BooleanField(default = False)
    second_vote_submit = models.BooleanField(default = False)
    discussion_submit = models.BooleanField(default = False)

    class Meta:
        unique_together =(('student', 'video'),)

    def __str__(self):
        return f"{self.student} in ({self.video.question})"



class DiscussionLink(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
	video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
	link = models.CharField(max_length = 255, null = True, blank = True)

	def __str__(self):
		return f"{self.group.section} in ({self.video.question})"
