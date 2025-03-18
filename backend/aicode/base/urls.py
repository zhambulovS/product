from django.urls import path, include
from .views import authView, home
from . import views

urlpatterns = [
    path("", home, name = "home"),
    path("sign-up/", authView, name = "authView"), 
    path("accounts/", include("django.contrib.auth.urls")),
    path('module2/topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]
 