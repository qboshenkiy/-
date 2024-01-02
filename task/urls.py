from django.urls import path
from .views import task_list, move_task, add_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('move/<int:task_id>/<str:status>/', move_task, name='move_task'),
    path('add/', add_task, name='add_task'),
]
