# courses/admin
from django.contrib import admin

from . import models

admin.site.register(models.Course)
admin.site.register(models.Lecture)
admin.site.register(models.Section)
admin.site.register(models.Group)
