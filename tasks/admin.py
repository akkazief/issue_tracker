from django.contrib import admin

from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'deadline')
    list_filter = ('title', 'status', 'deadline')
    search_fields = ('title', 'status', 'deadline')
    fields = ('title', 'status', 'deadline')

admin.site.register(Task, TaskAdmin)
