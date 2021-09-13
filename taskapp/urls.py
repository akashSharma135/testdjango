from django.urls import path
from .views import TaskView

urlpatterns = [
    path('add-task', TaskView.as_view())
]