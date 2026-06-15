from django.shortcuts import redirect, get_object_or_404, render

from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

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

class CreateIssueView(FormView):
    template_name = "issues/create_issue.html"
    form_class = IssueForm
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateIssueView(FormView):
    template_name = "issues/issue_update.html"
    form_class = IssueForm

    def dispatch(self, request, *args, **kwargs):
        self.issue = get_object_or_404(Issue, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def form_valid(self, form):
        issue = form.save()
        issue.type.set(form.cleaned_data['type'])
        return redirect('main')


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
