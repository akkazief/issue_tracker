from django.contrib import admin

from issues.models import Issue, Status, Type, Project


class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "summary", "status", "created_at", "updated_at")
    list_filter = ("status", "type")
    search_fields = ("summary", "description")

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start_date", "end_date")
    search_fields = ("name", "description")

admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project, ProjectAdmin)
