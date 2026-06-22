from django.urls import path
from issues.views.issues import (
    IssuesView,
    IssuesDetailView,
    CreateIssueView,
    UpdateIssueView,
    DeleteIssueView,
)

from issues.views.projects import (
    ProjectsView,
    ProjectDetailView,
    CreateProjectView,
    UpdateProjectView,
    DeleteProjectView,
)

urlpatterns = [
    # Проекты
    path("", ProjectsView.as_view(), name="projects_list"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project_details"),
    path("projects/create/", CreateProjectView.as_view(), name="create_project"),
    path("projects/<int:pk>/update/", UpdateProjectView.as_view(), name="update_project"),
    path("projects/<int:pk>/delete/", DeleteProjectView.as_view(), name="delete_project"),
    # Задачи

    path("issues/<int:pk>/", IssuesDetailView.as_view(), name="issue_details"),
    path("projects/<int:pk>/issues/create/",CreateIssueView.as_view(),name="create_issue",),
    path("issues/<int:pk>/update/", UpdateIssueView.as_view(), name="update_issue"),
    path("issues/<int:pk>/delete/", DeleteIssueView.as_view(), name="delete_issue"),
]