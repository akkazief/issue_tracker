from django.shortcuts import redirect
from django.views.generic import UpdateView
from issues.models import Issue
from issues.forms import IssueForm
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateIssueView(LoginRequiredMixin, UpdateView):
    template_name = "issues/issue_update.html"
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        issue = form.save()
        issue.type.set(form.cleaned_data['type'])
        return redirect("project_details", pk=issue.project.pk)
