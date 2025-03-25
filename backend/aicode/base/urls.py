from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import authView, home, tasks, course, compiler, profile, topic_detail, blog

urlpatterns = [
    path("", home, name="home"),
    path("tasks/", tasks, name="tasks"),
    path("blog/", blog, name="blog"),
    path("course/", course, name="course"),
    path("compiler/", compiler, name="compiler"),
    path("sign-up/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("profile/", profile, name="profile"),
    path("module2/topic/<int:topic_id>/", topic_detail, name="topic_detail"),
]
