from django.views.generic import ListView

from issues.models import Issue

from django.shortcuts import redirect


class IssuesView(ListView):
    template_name = "issues/issues.html"
    context_object_name = "issues"
    queryset = Issue.objects.all().order_by("-updated_at")

    def post(self, request, *args, **kwargs):
        id_list = request.POST.getlist("id_list")
        if id_list:
            Issue.objects.filter(id__in=id_list).delete()
        return redirect("projects_list")
