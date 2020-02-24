from django.contrib import admin

from . import models

class ResponseAdmin(admin.ModelAdmin):
    fields = ('question', 'contents', 'student', 'vote1', 'vote2', 'answer1', 'answer2', 'timestamp')
    readonly_fields = ('timestamp',)


admin.site.register(models.Question)
admin.site.register(models.Response, ResponseAdmin)
