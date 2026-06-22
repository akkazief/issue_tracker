from django.views.generic import DeleteView
from django.urls import reverse_lazy
from issues.models import Project


class DeleteProjectView(DeleteView):
    template_name = "projects/delete_project.html"
    model = Project
    context_object_name = "project"
    success_url = reverse_lazy("projects_list")
