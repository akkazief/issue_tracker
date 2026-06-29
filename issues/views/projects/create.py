from django.views.generic import CreateView
from django.urls import reverse_lazy
from issues.forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from issues.mixins import MemberRequiredMixin



class CreateProjectView(MemberRequiredMixin,LoginRequiredMixin, CreateView):
    permission_required = 'issues.add_project'

    template_name = "projects/create_project.html"
    form_class = ProjectForm
    success_url = reverse_lazy("projects_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response