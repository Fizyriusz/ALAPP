# aquan_lessons/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Lesson, LessonProgress, UserProgress
from .forms import UserRegisterForm

def home(request):
    lessons = Lesson.objects.all()  # Pobieranie wszystkich lekcji z bazy danych
    completed_lessons = []
    if request.user.is_authenticated:
        completed_lessons = LessonProgress.objects.filter(user=request.user, completed=True).values_list('lesson_id', flat=True)

    return render(request, 'aquan_lessons/home.html', {
        'lessons': lessons,
        'completed_lessons': completed_lessons,
    })

# Funkcja widoku dla konkretnej lekcji
@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    previous_lesson = Lesson.objects.filter(id__lt=lesson_id).order_by('-id').first()
    next_lesson = Lesson.objects.filter(id__gt=lesson_id).order_by('id').first()
    lessons = Lesson.objects.all()  # Pasek boczny

    # Sprawdzenie, czy użytkownik ukończył lekcję
    progress, created = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    if request.method == "POST":
        # Jeśli użytkownik przesłał formularz, oznaczamy lekcję jako ukończoną
        progress.completed = True
        progress.save()
        return redirect('lesson_detail', lesson_id=next_lesson.id) if next_lesson else redirect('home')

    return render(request, 'aquan_lessons/lesson_detail.html', {
        'lesson': lesson,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
        'lessons': lessons,
        'progress': progress,
    })

# Funkcja rejestracji użytkownika
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone dla {username}! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'aquan_lessons/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    completed_lessons = LessonProgress.objects.filter(user=user, completed=True)
    progress = UserProgress.objects.filter(user=user)
    lessons = Lesson.objects.all()  # Dodanie lekcji do paska bocznego

    return render(request, 'aquan_lessons/profile.html', {
        'user': user,
        'completed_lessons': completed_lessons,
        'progress': progress,
        'lessons': lessons,  # Przekazanie lekcji do paska bocznego
    })
