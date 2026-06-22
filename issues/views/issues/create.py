from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from issues.models.project import Project
from issues.forms import IssueForm


class CreateIssueView(CreateView):
    template_name = "issues/create_issue.html"
    form_class = IssueForm

    def get_success_url(self):
        return reverse_lazy("project_details", kwargs={"pk": self.project.pk})

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        issue = form.save(commit=False)
        issue.project = self.project
        issue.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        return context
