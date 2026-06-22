from django.urls import reverse_lazy
from django.views.generic import CreateView

from issues.forms import IssueForm



class CreateIssueView(CreateView):
    template_name = "issues/create_issue.html"
    form_class = IssueForm
    success_url = reverse_lazy("main")