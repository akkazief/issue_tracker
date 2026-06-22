from django.views.generic import UpdateView
from django.urls import reverse_lazy
from issues.models import Project
from issues.forms import ProjectForm


class UpdateProjectView(UpdateView):
    template_name = "projects/project_update.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy("project_details", kwargs={"pk": self.object.pk})
