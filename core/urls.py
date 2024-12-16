from django.urls import path
from .views import *

urlpatterns = [
    # User endpoints
    path('users/register/', RegisterUserView.as_view(), name='register-user'),
    path('users/login/', LoginUserView.as_view(), name='login-user'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),

    # Project endpoints
    path('projects/', ProjectListCreateView.as_view(), name='list-create-projects'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),

    # Task endpoints
    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='list-create-tasks'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),

    # Comment endpoints
    path('tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='list-create-comments'),
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment-detail'),
]
