from urllib.parse import urlencode
from django.db.models import Q
from issues.models import SimpleSearchForm
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
        return redirect("main")

#
# class IssuesView(ListView):
#     template_name = "articles/index.html"
#     model = Issue
#     context_object_name = "issues"
#     ordering = ["-created_at"]
#     queryset = Issue.objects.all()
#     paginate_by = 5
#     paginate_orphans = 1
#
#     def dispatch(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_search_form(self):
#         return SimpleSearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search']
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         if self.search_value:
#             queryset = queryset.filter(
#                 Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value)
#             )
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['search_form'] = self.form
#
#         if self.search_value:
#             context['query'] = urlencode({"search": self.search_value})
#             context['search_value'] = self.search_value
#         return context