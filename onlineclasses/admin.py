from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Video)
admin.site.register(models.DiscussionLink)
#admin.site.register(models.VideoTracker)

