from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from issues.models import Project

from issues.mixins import MemberRequiredMixin




class DeleteProjectView(MemberRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "issues.delete_project"

    template_name = "projects/delete_project.html"
    model = Project
    context_object_name = "project"
    success_url = reverse_lazy("projects_list")
