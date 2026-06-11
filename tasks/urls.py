from django.urls import path
from tasks.views import tasks, create_task, delete_task, details, update_task

urlpatterns = [
    path('', tasks, name='main'),
    path('create_task/', create_task, name='create_task'),
    path('tasks/<int:pk>/', details, name='details'),
    path('tasks/<int:pk>/update', update_task, name='update_task'),
    path('tasks/<int:pk>/delete', delete_task, name='delete_task'),
]