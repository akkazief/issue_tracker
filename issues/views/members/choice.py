from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from issues.forms import ProjectMembersForm
from issues.models import Project


from django.contrib.auth.mixins import LoginRequiredMixin
from issues.mixins import MemberRequiredMixin



User = get_user_model()


class ProjectMembersView(MemberRequiredMixin,LoginRequiredMixin,View):
    permission_required = 'issues.manage_members'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectMembersForm(initial={"members": project.members.all()})
        return render(request, "projects/members_managment.html", {
            "project": project,
            "form": form,
        })

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectMembersForm(request.POST)
        if form.is_valid():
            project.members.set(form.cleaned_data["members"])
            return redirect("project_members_list", pk=pk)
        return render(request, "projects/members_managment.html", {
            "project": project,
            "form": form,
        })