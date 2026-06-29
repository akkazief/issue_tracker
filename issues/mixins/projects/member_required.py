from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from issues.models import Project
from issues.models import Issue


class MemberRequiredMixin:
    permission_required = None

    def get_project(self):
        if "pk" in self.kwargs:
            project = Project.objects.filter(pk=self.kwargs["pk"]).first()
            if project:
                return project
            issue = get_object_or_404(Issue, pk=self.kwargs["pk"])
            return issue.project

        raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if self.permission_required and not request.user.has_perm(self.permission_required):
            raise PermissionDenied
        if self.kwargs:
            project = self.get_project()
            if not project.members.filter(pk=request.user.pk).exists():
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)