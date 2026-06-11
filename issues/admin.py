from django.contrib import admin

from issues.models import Issue
from issues.models import Status
from issues.models import Type

class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'status', 'type', 'created_at', 'updated_at')
    list_filter = ('status', 'type')
    search_fields = ('summary', 'description')

admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
