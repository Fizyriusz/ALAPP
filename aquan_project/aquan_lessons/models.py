from django.db import models
from django.contrib.auth.models import User

# Definicja modelu Module
class Module(models.Model):
    title = models.CharField(max_length=200)  # Tytuł modułu
    description = models.TextField()  # Opis modułu
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia
    updated_at = models.DateTimeField(auto_now=True)  # Data ostatniej aktualizacji

    def __str__(self):
        return self.title

# Definicja modelu Lesson
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons", null=True, blank=True)  # Powiązanie lekcji z modułem
    title = models.CharField(max_length=200)  # Tytuł lekcji
    content = models.TextField()  # Treść lekcji
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia
    updated_at = models.DateTimeField(auto_now=True)  # Data ostatniej aktualizacji

    def __str__(self):
        return self.title

# Definicja modelu Quiz
class Quiz(models.Model):
    title = models.CharField(max_length=200)  # Tytuł quizu
    questions = models.TextField()  # Pytania do quizu (w przyszłości można zmienić na bardziej złożony model)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Definicja modelu LessonProgress
class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {'Completed' if self.completed else 'In Progress'}"

# Definicja modelu UserProgress
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)  # Dodajemy moduł do postępu użytkownika
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)  # Dodajemy quiz do postępu użytkownika
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed')])
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Progress for {self.user.username} - {self.lesson or self.module or self.quiz}"
