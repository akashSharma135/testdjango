from django.urls import path
from .views import AllManagersView, AllSimpleUserView, LoginView, ProfileView, UserDetailView, UserRegisterView, AssignManagerView

urlpatterns = [
    path('register', UserRegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', ProfileView.as_view()),
    path('all-managers', AllManagersView.as_view()),
    path('all-users', AllSimpleUserView.as_view()),
    path('user', UserDetailView.as_view()),
    path('assign-manager', AssignManagerView.as_view()),
    # path('assign-task', AssignTaskView.as_view())
]