from django.views.generic import DeleteView

from django.urls import reverse_lazy

from issues.models import Issue


class DeleteIssueView(DeleteView):
    template_name = "issues/delete_issue.html"
    model = Issue
    context_object_name = "issue"

    def get_success_url(self):
        return reverse_lazy("project_details", kwargs={"pk": self.object.project.pk})