from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'complete', 'created_on', 'udpated_on')
    list_display_links = ('user', 'title', 'complete',
                          'created_on', 'udpated_on')



