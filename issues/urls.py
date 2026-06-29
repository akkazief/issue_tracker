from django.urls import path
from issues.views.issues import (
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

from issues.views.members import (
    ProjectMembersListView,
    ProjectMembersView
)

urlpatterns = [
    # Проекты
    path("", ProjectsView.as_view(), name="projects_list"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project_details"),
    path("projects/create/", CreateProjectView.as_view(), name="create_project"),
    path("projects/<int:pk>/update/", UpdateProjectView.as_view(), name="update_project"),
    path("projects/<int:pk>/delete/", DeleteProjectView.as_view(), name="delete_project"),
    # Участники проектов
    path("projects/<int:pk>/members/", ProjectMembersView.as_view(), name="project_members"),
    path("projects/<int:pk>/members/list", ProjectMembersListView.as_view(), name="project_members_list"),
    # Задачи
    path("issues/<int:pk>/", IssuesDetailView.as_view(), name="issue_details"),
    path("projects/<int:pk>/issues/create/",CreateIssueView.as_view(),name="create_issue",),
    path("issues/<int:pk>/update/", UpdateIssueView.as_view(), name="update_issue"),
    path("issues/<int:pk>/delete/", DeleteIssueView.as_view(), name="delete_issue"),
]