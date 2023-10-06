from django.urls import path

from todo.views import TaskListView, TaskCreateView, task_done_not_done, TagsListView, TagCreateView


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("task-complete/<int:pk>/", task_done_not_done, name="task-complete"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tag-create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"
