from django.urls import path
from issues.views.issues import (
    IssuesView,
    IssuesDetailView,
    CreateIssueView,
    UpdateIssueView,
    DeleteIssueView,
)


urlpatterns = [
    path("", IssuesView.as_view(), name="main"),
    path("<int:pk>/", IssuesDetailView.as_view(), name="details"),
    path("create/", CreateIssueView.as_view(), name="create_issue"),
    path("<int:pk>/update/", UpdateIssueView.as_view(), name="update_issue"),
    path("<int:pk>/delete/", DeleteIssueView.as_view(), name="delete_issue"),
]
