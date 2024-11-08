# aquan_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aquan_lessons.urls')),  # Dodajemy aplikację aquan_lessons
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Przekierowanie do logowania po wylogowaniu
]
