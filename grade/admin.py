from django.contrib import admin

from . import models

class AttendanceAdmin(admin.ModelAdmin):

    fields = ('student', 'status', 'datestamp')



# Register your models here.
admin.site.register(models.Grade)
admin.site.register(models.AttendanceInstance,AttendanceAdmin)

