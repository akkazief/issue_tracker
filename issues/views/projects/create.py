from django.views.generic import CreateView
from django.urls import reverse_lazy
from issues.forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateProjectView(LoginRequiredMixin, CreateView):
    template_name = "projects/create_project.html"
    form_class = ProjectForm
    success_url = reverse_lazy("projects_list")