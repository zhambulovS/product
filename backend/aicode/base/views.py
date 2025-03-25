from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import never_cache
@never_cache
def home(request):
    return render(request, "home.html")

@login_required
def profile(request):
    return render(request, "nav/profile.html")

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/sign-up.html", {"form": form})
@never_cache
def tasks(request):
    return render(request, "nav/tasks.html")
@never_cache
def blog(request):
    return render(request, "nav/blog.html")
@never_cache
def course(request):
    return render(request, "nav/course.html")
@never_cache
def compiler(request):
    return render(request, "nav/compiler.html")
@never_cache
def topic_detail(request, topic_id):
    topics = {
        4: {
            "topic_title": "4 Тақырып: Адам-компьютер өзара әрекеттестігі",
            "video_url": "https://www.youtube.com/embed/29gjnUB4Tds?si=CxPid1brPTihDVfX",
            "tasks": ["Task 4.1", "Task 4.2", "Task 4.3"],
        },
        5: {
            "topic_title": "5 Тақырып: Деректер қорларының жүйелері",
            "video_url": "https://www.youtube.com/embed/OiodPKcCQoA?si=JgLc8mTaa4gJUEXK",
            "tasks": ["Task 5.1", "Task 5.2", "Task 5.3"],
        },
        6: {
            "topic_title": "6 Тақырып: Деректерді талдау. Деректерді басқару.",
            "video_url": "https://www.youtube.com/embed/-vTjhRKRxsU?si=A3QTkoYB88WSgThe",
            "tasks": ["Task 6.1", "Task 6.2"],
        },
    }
    context = topics.get
