from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Strona główna
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),  # Strona szczegółów lekcji
]

urlpatterns = [
    path('', views.home, name='home'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('register/', views.register, name='register'),  # Rejestracja użytkownika
    path('login/', auth_views.LoginView.as_view(template_name='aquan_lessons/login.html'), name='login'),  # Logowanie użytkownika
    path('logout/', auth_views.LogoutView.as_view(template_name='aquan_lessons/logout.html'), name='logout'),  # Wylogowanie użytkownika
    path('profile/', views.profile, name='profile'),  # Profil użytkownika
]