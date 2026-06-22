from django.views.generic import DetailView
from issues.models.project import Project


class ProjectDetailView(DetailView):
    template_name = "projects/project_details.html"
    model = Project
    context_object_name = "project"
