from django.contrib import admin
from django.utils.html import format_html
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'colored_status',
                    'created_on', 'udpated_on')
    list_display_links = ('user', 'title', 'colored_status',
                          'created_on', 'udpated_on')
    date_hierarchy = 'created_on'
    list_filter = ('complete', 'user')

    def colored_status(self, obj):
        if obj.complete:
            return format_html(
                '<span style="color: green;">{}</span>',
                (obj.complete),
            )
        else:
            return format_html(
                '<span style="color: red;">{}</span>',
                (obj.complete),
            )



