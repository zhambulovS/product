from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . import views


@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/sign-up.html", {"form": form})

def topic_detail(request, topic_id):
    # Пример: упрощённая логика, без БД
    if topic_id == 4:
        context = {
            'topic_title': '4 Тақырып: Адам-компьютер ӛзара әрекеттестігі',
            'video_url': 'https://www.youtube.com/embed/EXAMPLE_VIDEO_4',
            'tasks': ['Task 4.1', 'Task 4.2', 'Task 4.3']
        }
    elif topic_id == 5:
        context = {
            'topic_title': '5 Тақырып: Деректер қорларының жүйелері',
            'video_url': 'https://www.youtube.com/embed/EXAMPLE_VIDEO_5',
            'tasks': ['Task 5.1', 'Task 5.2', 'Task 5.3']
        }
    elif topic_id == 6:
        context = {
            'topic_title': '6 Тақырып: Деректерді талдау. Деректерді басқару.',
            'video_url': 'https://www.youtube.com/embed/EXAMPLE_VIDEO_6',
            'tasks': ['Task 6.1', 'Task 6.2']
        }
    else:
        return render(request, '404.html', status=404)
    
    return render(request, 'topic_details.html', context)