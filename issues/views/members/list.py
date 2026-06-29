from django.shortcuts import get_object_or_404, render
from django.views import View
from issues.models import Project


class ProjectMembersListView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        members = project.members.all()
        return render(request, "projects/members_list.html", {
            "project": project,
            "members": members,
        })
