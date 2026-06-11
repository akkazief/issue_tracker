from django.shortcuts import redirect, get_object_or_404, render

from django.views.generic import TemplateView

from issues.models.issue import Issue
from issues.forms import IssueForm


class IssuesView(TemplateView):
    template_name = "issues/issues.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issues"] = Issue.objects.all().order_by("-updated_at")
        return context

    def post(self, request, *args, **kwargs):
        id_list = request.POST.getlist("id_list")
        if id_list:
            Issue.objects.filter(id__in=id_list).delete()
        return redirect("main")


class IssuesDetailView(TemplateView):
    template_name = "issues/issue_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=self.kwargs.get("pk"))
        return context


class CreateIssueView(TemplateView):
    template_name = "issues/create_issue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)

        if form.is_valid():
            issue = form.save()
            issue.type.set(form.cleaned_data['type'])
            return redirect('main')
        return render(request, 'issues/create_issue.html', {'form': form})


class UpdateIssueView(TemplateView):
    template_name = "issues/issue_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=self.kwargs.get("pk"))
        context["issue"] = issue
        context["form"] = IssueForm(instance=issue)
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=self.kwargs.get("pk"))
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save()
            issue.type.set(form.cleaned_data['type'])
            return redirect('main')
        return render(request, 'issues/create_issue.html', {'form': form})


class DeleteIssueView(TemplateView):
    template_name = "issues/delete_issue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=self.kwargs.get("pk"))
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=self.kwargs.get("pk"))
        issue.delete()
        return redirect("main")
