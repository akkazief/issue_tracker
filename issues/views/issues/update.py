from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from issues.models import Issue
from issues.forms import IssueForm


class UpdateIssueView(UpdateView):
    template_name = "issues/issue_update.html"
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        issue = form.save()
        issue.type.set(form.cleaned_data["type"])
        return redirect("project_details", pk=issue.project.pk)
