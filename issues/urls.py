from django.urls import path
from issues.views import issues, create_issue, delete_issue, details, update_issue

urlpatterns = [
    path('', issues, name='main'),
    path('create_issue/', create_issue, name='create_issue'),
    path('issues/<int:pk>/', details, name='details'),
    path('issues/<int:pk>/update', update_issue, name='update_issue'),
    path('issues/<int:pk>/delete', delete_issue, name='delete_issue'),
]