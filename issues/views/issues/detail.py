from django.views.generic import DetailView
from issues.models import Issue

class IssuesDetailView(DetailView):
    template_name = "issues/issue_details.html"
    model = Issue
    context_object_name = "issue"